import requests, json, re


class pyssh:
    def __init__(
        self,
        domain: str,
        token: str,
        port: int,
        verified: bool = False,
    ) -> None:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        """
        self.port = port
        self.token = token
        self.domain = domain
        if verified:
            self.verified = 'https'
        else:
            self.verified = 'http'

    def GetList(
            self) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        response = requests.request("GET", "{}://{}:{}/api/{}/listuser".format(
            self.verified, self.domain, self.port, self.token)).text
        if "Limit Access" in response:
            return "[401 Unauthorized]: The TOKEN is Not Valid!"
        else:
            return response

    def AddClient(
            self,
            username: str,
            password: str,
            Traffic: str,
            IpLimit: str,
            expdate: str,
            Email: str = '',
            PhoneNumber: str = '',
            connection_start: str = ''
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            username (``str``):
                the user you want to make changes for.

            password (``str``):
                give him/her a password for its connection.

            verified (``bool``, optional):
               https or http that has been set in cloudflare

            IpLimit (``int``):
                count of allowed Ip's to connect at the same time

            Email (``str``, optional):
                additional information for users

            PhoneNumber (``str``, optional):
                additional information for users

            traffic (``str``):
                allowed traffic for user in 'mb' format

            expdate (``str``):
                ex date (format 2023-07-04)

            connection_start (``str``, optional):
                If you want to set the expdate on the first connection, enter the number of validity days

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token,
                   'username': username,
                   'password': password,
                   'email': Email,
                   'mobile': PhoneNumber,
                   'multiuser': IpLimit,
                   'traffic': Traffic,
                   'type_traffic': 'mb',
                   'expdate': expdate,
                   'connection_start': connection_start}

        url = "{}://{}:{}/api/adduser".format(
            self.verified, self.domain, self.port)
        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def RemoveClient(
            self,
            username: str,
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token, 'username': username}
        url = "{}://{}:{}/api/delete".format(self.verified,
                                             self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def GetClient(
            self,
            username: str,
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """
        url = "{}://{}:{}/api/{}/user/{}".format(
            self.verified, self.domain, self.port, self.token, username)
        response = requests.request("GET", url, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def EditClient(
            self,
            username: str,
            password: str,
            Traffic: str,
            IpLimit: str,
            expdate: str,
            Email: str = '',
            PhoneNumber: str = '',
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            username (``str``):
                the user you want to make changes for.

            password (``str``):
                give him/her a password for its connection.

            verified (``bool``, optional):
               https or http that has been set in cloudflare

            IpLimit (``int``):
                count of allowed Ip's to connect at the same time

            Email (``str``, optional):
                additional information for users

            PhoneNumber (``str``, optional):
                additional information for users

            traffic (``str``):
                allowed traffic for user in 'mb' format

            expdate (``str``):
                ex date (format 2023-07-04)

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token,
                   'username': username,
                   'password': password,
                   'email': Email,
                   'mobile': PhoneNumber,
                   'multiuser': IpLimit,
                   'traffic': Traffic,
                   'type_traffic': 'mb',
                   'expdate': expdate}

        url = "{}://{}:{}/api/edituser".format(
            self.verified, self.domain, self.port)
        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def ActiveClient(
            self,
            username: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token, 'username': username}
        url = "{}://{}:{}/api/active".format(self.verified,
                                             self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def DectiveClient(
            self,
            username: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token, 'username': username}
        url = "{}://{}:{}/api/deactive".format(
            self.verified, self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def ResetTraffic(
            self,
            username: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {'token': self.token, 'username': username}
        url = "{}://{}:{}/api/retraffic".format(
            self.verified, self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def Renewal(
            self,
            username: str,
            day_date: str,
            re_date: bool,
            re_traffic: bool,
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

            day_date (``str``):
                Credit in the form of days.

            red_date (``bool``):
                Update the registration date to today.

            re_traffic  (``bool``):
                Reset the traffic.

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {
            'token': self.token,
            'username': username,
            'day_date': day_date,
            're_date': 'yes' if re_date else 'no',
            're_traffic': 'yes' if re_traffic else 'no'}
        url = "{}://{}:{}/api/renewal".format(
            self.verified, self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def AddTraffic(
            self,
            username: str,
            traffic: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

            traffic (``str``):
                allowed traffic for user in 'mb' format

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        payload = {
            'token': self.token,
            'username': username,
            'traffic ': traffic,
            'type_traffic ': 'mb'}
        url = "{}://{}:{}/api/traffic".format(
            self.verified, self.domain, self.port)

        response = requests.request(
            "POST", url, data=payload, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def OnlineUsers(
            self,
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        url = "{}://{}:{}/api/{}/online".format(
            self.verified, self.domain, self.port, self.token)

        response = requests.request("GET", url, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def KillUser(
            self,
            username: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            username (``str``):
                the user you want to make changes for.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        url = "{}://{}:{}/api/{}/kill/user/{}".format(
            self.verified, self.domain, self.port, self.token, username)

        response = requests.request("GET", url, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def KillPid(
            self,
            PID: str
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            PID (``str``):
                system PID.

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        url = "{}://{}:{}/api/{}/kill/id/{}".format(
            self.verified, self.domain, self.port, self.token, PID)

        response = requests.request("GET", url, verify=self.verified).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            return response

    def Filtering(
            self
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """

        url = "{}://{}:{}/api/{}/filtering".format(
            self.verified, self.domain, self.port, self.token)
        response = requests.get(url).text

        if "Limit Access" in response:
            return "[BadLogin]: The TOKEN is Not Valid!"
        else:
            checks = json.loads(response)
            places = []
            for check in checks:
                if not check['status'] == 'Online':
                    places.append(f"{check['location']} is {check['status']}")
            else:
                places.append("everything is ok!")
            problems = ''
            for place in places:problems += f'-> {place}\n'     
            return problems

    def DownloadDataBase(
            self
    ) -> requests.Response:
        """Get existing clients from the list.

        Parameters:
            domain (``str``):
                domain of your Xpanel

            token (``str``):
               token of the your API

            port (``int``):
               port of Xpanel 

            verified (``bool``, optional):
               https or http that has been set in cloudflare

        Returns:
            `~Dict`: On success, a List is returned or else 404 an error will be raised
        """
        
        url = "{}://{}:{}/api/{}/backup".format(
            self.verified, self.domain, self.port, self.token)
        fileName = re.sub(r'(.+/dl/)', '', ((json.loads(requests.get(url).text)["link"]).replace('\\', '')))
        url = f'{self.verified}://{self.domain}:{self.port}/api/{self.token}/backup/dl/{fileName}'
        
        
        with open(fileName, 'w') as database:
            database.write(requests.get(url).text)
            database.close()
        return 'file [%s] saved!'%fileName

