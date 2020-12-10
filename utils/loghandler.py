import datetime
def main(error):
    refreshed_time = str(datetime.datetime.now().date())
    log_write = open("logs/LOG "+refreshed_time+".txt", "a+")
    string = str(error)
    log_write.write("\nLOGGED -"+refreshed_time+" - "+string)
    log_write.close()