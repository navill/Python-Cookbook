"""
처리해야할 데이터의 크기가 매우 커서 메모리에 한꺼번에 올라가지 않아 데이터 처리 파이프라인과 같은 방식으로 처리하고자 할 때
yield from: https://www.notion.so/afmadadans/Chapter-16-dbc3ca6c59fc4e02ad1193f3ac38cad5#e6622a7edadc48668b6ffc3146545656
"""

import bz2
import fnmatch
import gzip
import os
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)  # yield


def gen_opener(filenames):
    # 다음 순환으로 넘어가기전에 파일이 닫히기 때문에 주의 -> itertools.chain 사용 불가
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f  # yield
        f.close()


def gen_concatenate(iterators):
    # 이터레이터 시퀀스를 단일 시퀀스로 통합
    for it in iterators:
        yield from it  # yield


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line  # yield


if __name__ == '__main__':

    # 각 함수는 제너레이터 객체를 반환한다.
    lognames = gen_find('access-log*', 'www')
    print(lognames)
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    # 각 함수의 제너레이터가 아래의 순환문에 의해 값을 생성하고 소비한다.
    for line in pylines:
        print(line)

    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))
