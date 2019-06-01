from subprocess import check_output, CalledProcessError

VERSION_FILE = '.version'
GIT_COMMAND = 'git describe --tags --long --dirty'
VERSION_FORMAT = '{tag}.dev{commit_count}+{commit_hash}'


def git_version() -> str:
    """
    Return package version from git, write commit to file
    """

    output = check_output(GIT_COMMAND.split()).decode('utf-8').strip().split('-')
    tag, count, commit = output[:3]
    dirty = len(output) == 4

    if count == '0' and not dirty:
        return tag
    return VERSION_FORMAT.format(tag=tag, commit_count=count, commit_hash=commit)


def get_version() -> str:
    """
    Get package version
    """
    try:
        version = git_version()
    except CalledProcessError:
        with open(VERSION_FILE, 'r') as f:
            version = f.readline().strip()
    else:
        with open(VERSION_FILE, 'w') as f:
            f.write(version)
    return version
