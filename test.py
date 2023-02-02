from updater4pyi import upd_source, upd_core
from updater4pyi.upd_iface_pyqt4 import UpdatePyQt4Interface



swu_source = upd_source.UpdateGithubReleasesSource('https://github.com/munindra-pwc/auto_update_test.git')
swu_updater = upd_core.Updater(current_version=...,
                               update_source=swu_source)
swu_interface = UpdatePyQt4Interface(swu_updater,
                                     progname='Your Project Name',
                                     ask_before_checking=True,
                                     parent=None)



print("Hi")