import datetime
import pytz

tday = datetime.date.today()

tdelta = datetime.timedelta(hours=12)

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday

t = datetime.time(9, 30, 45, 100000)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
