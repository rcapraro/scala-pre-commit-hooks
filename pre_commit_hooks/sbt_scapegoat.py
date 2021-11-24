from pre_commit_hooks.sbt_runner import run_sbt_command
from colorama import init as colorama_init, Fore

TASK_SCAPEGOAT= 'scapegoat'
MISSING_PLUGIN_CHECK_STRING = 'Not a valid key: scapegoat'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: scapegoat SBT plugin not present! See {Fore.BLUE}https://github.com/scapegoat-scala/sbt-scapegoat{Fore.RED} for installation instructions.'


def main():
    colorama_init()

    return run_sbt_command(f'; {TASK_SCAPEGOAT}', MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
