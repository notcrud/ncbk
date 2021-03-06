#from crontab import CronTab
from plan import Plan

'''
This script uses python-crontab to run a cron job every day at noon,
to save a dump of all the keys in the Redis datastore that's used 
by notCRUD.
'''

'''
tab = CronTab(user='rudimk')
command = '/usr/bin/redis-cli bgsave'
cron_job = tab.new(cmd, comment='This command dumps Redis keys and saves them.')
cron_job.minute().on(0)
cron_job.hour().on(12)
'''

cron = Plan()
cron.command('/usr/bin/redis-cli bgsave', every='1.day', at='12:00')

if __name__ == '__main__':
	cron.run('write')