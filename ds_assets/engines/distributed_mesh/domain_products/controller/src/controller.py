from ds_discovery import Controller
import os
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

__author__ = 'Darryl Oatridge'


def domain_controller(**kwargs):
    uri_pm_repo = os.getenv('HADRON_PM_REPO')
    # extract any kwargs
    hadron_kwargs = kwargs.copy()
    # pop the run_controller attributes from the kwargs
    run_book = hadron_kwargs.pop('runbook', None)
    mod_tasks = hadron_kwargs.pop('mod_tasks', None)
    repeat = hadron_kwargs.pop('repeat', None)
    sleep = hadron_kwargs.pop('sleep', None)
    run_time = hadron_kwargs.pop('run_time', None)
    run_cycle_report = hadron_kwargs.pop('run_cycle_report', None)
    source_check_uri = hadron_kwargs.pop('source_check_uri', None)

    # instantiate the Controller passing any remaining kwargs
    controller = Controller.from_env(uri_pm_repo=uri_pm_repo, default_save=False, has_contract=True, **hadron_kwargs)
    # run the controller nano services.
    controller.run_controller(run_book=run_book, mod_tasks=mod_tasks, repeat=repeat, sleep=sleep, run_time=run_time,
                              source_check_uri=source_check_uri, run_cycle_report=run_cycle_report)


if __name__ == '__main__':
    domain_controller()
