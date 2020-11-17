import requests


class TeamCity:
    """
    For the full reference please check out the official JetBrains documentation:
    https://www.jetbrains.com/help/teamcity/rest-api-reference.html
    """

    __headers = {
        "json": {"Content-Type": "application/json", "Accept": "application/json"},
        "xml": {"Content-Type": "application/xml", "Accept": "application/xml"},
    }

    def __init__(
        self,
        username=None,
        password=None,
        token=None,
        host="localhost",
        port=8111,
        accept_type="json",
    ):
        self.url = f"http://{host}:{port}/app/rest"
        self.accept_type = accept_type
        self.username = username
        self.password = password
        self.token = token
        self.headers = self.__headers[accept_type]
        self.__session = self.__start_session()

    def __token_auth(self):
        self.headers["Authorization"] = f"Bearer {self.token}"

    def __start_session(self):
        session = requests.Session()
        if self.token:
            self.__token_auth()
        else:
            session.auth = (self.username, self.password)
        return session

    def __get(self, endpoint, params=None):
        endpoint = f"{self.url}/{endpoint}"
        return self.__session.get(endpoint, headers=self.headers, params=params)

    def custom_request(
        self, endpoint, method="GET", headers=None, params=None, data=None
    ):
        headers = headers or self.headers
        endpoint = f"{self.url}/{endpoint}"
        return self.__session.request(
            method=method, url=endpoint, headers=headers, params=params, data=data
        )

    def get_api_info(self):
        if self.accept_type == "json":
            endpoint = "swagger.json"
        else:
            endpoint = "application.wadl"
        return self.__get(endpoint)

    def get_server_info(self):
        endpoint = "server"
        return self.__get(endpoint)

    """
    ================================================
    Projects and Build Configuration/Templates Lists
    ================================================
    """

    def get_projects(self):
        """
        List of projects
        """
        endpoint = "projects"
        return self.__get(endpoint)

    def get_project(
        self,
        project_locator,
    ):
        """
        Project details
        where project_locator can be id:<internal_project_id> or name:<project%20name>
        :param project_locator: str
        :return:
        """
        endpoint = f"projects/{project_locator}"
        return self.__get(endpoint)

    def get_build_types(self):
        """
        List of build configurations
        :return:
        """
        endpoint = "buildTypes"
        return self.__get(endpoint)

    def get_project_build_types(self, project_locator):
        """
        List of build configurations of a project
        :param project_locator: str
        :return:
        """
        endpoint = f"projects/{project_locator}/buildTypes"
        return self.__get(endpoint)

    # TODO: Project Settings
    """
    ================
    Project Settings
    ================
    """

    # TODO: Project Features
    """
    ================
    Project Features
    ================
    """

    # TODO: VCS Roots
    """
    =========
    VCS Roots
    =========
    """
    # TODO: Cloud Profiles
    # TODO: Build Configuration And Template Settings
    # TODO: Build Requests
    # TODO: Tests and Build Problems
    # TODO: Investigations
    # TODO: Agents
    """
    ======
    Agents
    ======
    """

    def get_agents(self, locator=None):
        """
        List agents (only authorized agents are included by default)
        :return:
        """
        endpoint = "agents"
        params = {}
        if locator:
            params["locator"] = locator
        return self.__get(endpoint, params)

    def get_agent(self, agent_locator):
        """

        :param agent_locator:
        :return:
        """
        endpoint = f"agents/{agent_locator}"
        return self.__get(endpoint)

    # TODO: Users
    # TODO: Audit Records
    # TODO: Data Backup
    # TODO: Typed Parameters Specification
    # TODO: Build Status Icon
    # TODO: TeamCity Licensing Information Requests
    # TODO: CCTray