#!/usr/bin/env python
from resource_management import Script
from resource_management.core.logger import Logger
from resource_management.core.resources.system import Execute

class Supervisor(Script):

    def install(self, env):
        import params
        Logger.info("Installing Supervisor packages")
        self.install_packages(env)
    def stop(self, env):
        Logger.info("Stopping Supervisor daemon")
        Execute("service supervisor stop")
        Logger.info("Stopping Supervisor daemon - DONE ")
    def start(self, env):
        Logger.info("Starting Supervisor daemon")
        Execute("service supervisor start")
        Logger.info("Starting Supervisor daemon - DONE ")
    def status(self, env):
        Logger.info("Getting status for Supervisor daemon")
        try:
            Execute("service supervisor status")
        except Fail:
            raise ComponentIsNotRunning()
        Logger.info("Getting status for Supervisor daemon - DONE ")

if __name__ == "__main__":
    Supervisor().execute()
