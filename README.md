# PySSH 
An application coded with python that allows you to modify your Xpanel ([Xpanel](https://github.com/xpanel-cp/XPanel-SSH-User-Management))

## How To Use
- clone the repository
``` bash
git clone https://github.com/Liwyd/pyssh.git
```
- Import pyssh in your .py file
```python
from pyssh import pyssh

# Setup a login
panel = ssh(
    domain="liwyd.com",
    token="ThisIsATokenForTest",
    port=80
    verified=False # Remember the ' verified ' option is not compulsory !
)
```


- Get clients list
```python
GetList = panel.GetList()

# Result

[
    {
        "id":3,
"username":"liwyd",
"password":"liwydpasswd",
"email":null,
"mobile":null,
"multiuser":"5",
"start_date":"2023-10-05",
"end_date":"2067-07-05",
"date_one_connect":"0",
"customer_user":"Ali",
"status":"active",
"traffic":"102400",
"referral":"",
"desc":null,
"created_at":"2023-10-05T11:34:53.000000Z",
"updated_at":"2023-10-05T21:02:03.000000Z",
"traffics":[{"id":3,
"username":"liwyd",
"download":"3559",
"upload":"7127",
"total":"10686",
"created_at":"2023-10-05T11:34:53.000000Z",
"updated_at":"2023-10-10T19:23:34.000000Z"}]}]
```

- Add client
```python
get = panel.AddClient(
    username='test',
    password="test123",
    Traffic = "5000",# in megabytes
    IpLimit = "1",
    expdate = "2023-07-04",
    Email="example@gmal.com",
    PhoneNumber = "095368709120",
    connection_start = "30", # If you want to set the expdate on the first connection, enter the number of validity days
)
```

- Edit the existing client
```python
get = panel.AddClient(
    username='test',
    password="test123",
    Traffic = "5000",# in megabytes
    IpLimit = "1",
    expdate = "2023-07-04",
    Email="example@gmal.com",
    PhoneNumber = "095368709120"
)
```

- Get client's information:
```python
GetClient = panel.GetClient(
    username="liwyd",
)

# Result
[
    {
        "id":3,
        "username":"liwyd",
        "password":"liwydpasswd",
        "email":null,
        "mobile":null,
        "multiuser":"5",
        "start_date":"2023-10-05",
        "end_date":"2067-07-05",
        "date_one_connect":"0",
        "customer_user":"Ali",
        "status":"active",
        "traffic":"102400",
        "referral":"",
        "desc":null,
        "created_at":"2023-10-05T11:34:53.000000Z",
        "updated_at":"2023-10-05T21:02:03.000000Z",
        "traffics":[{"id":3,"username":"liwyd",
        "download":"3562","upload":"7137",
        "total":"10699",
        "created_at":"2023-10-05T11:34:53.000000Z",
        "updated_at":"2023-10-10T19:36:50.000000Z"}]},
        {"port_direct":"2794",
        "port_tls":"444",
        "port_dropbear":"2792",
        "message":"success"
    }
]

```

- Active/Dective client:
```python
active = panel.ActiveClient(
    username="liwyd",
)

dective = panel.DectiveClient(
    username="liwyd",
)
```

- Delete existing client:
```python
get = panel.RemoveClient(
    username="liwyd",
)
```

- Reset existing client's Traffic:
```python
get = panel.ResetTraffic(
    username="liwyd",
)
```

- Add Traffic to existing client:
```python
get = panel.AddTraffic(
    username="liwyd",
    traffic="5000",# in megabytes
)
```
- Renewal the existing client:
```python
get = panel.Renewal(
    username="liwyd",
    day_date="5", #Credit in the form of days.
    re_date=False,
    re_traffic=False,
)
```
- KillUser:
```python
get = panel.KillUser(
    username="liwyd",
)
```
- KillPID:
```python
get = panel.KillPid(
    PID="liwyd",
)
```

# Get the Online users

```python
users = panel.OnlineUsers()
```
# Check the filtering status
```python
get = panel.Filtering()

# Result:
"[STATUS]: everything is ok!"
```
# Download DataBase
```python
get = panel.DownloadDataBase()

# Result:
"file [XPanel-2023-10-10---06-22-14.sql] saved!"
```
