import log_system

Logger = log_system.Logger()
Logger.start_log()

Logger.log_info(message="Test")

Logger.log_close_log()
