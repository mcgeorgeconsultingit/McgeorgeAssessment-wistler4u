import xmlrpc.client


class CourseManger:
    def __init__(self, url: str="http://0.0.0.0:8016", db: str="odoodb", username: str = "odoouser", password: str= "adminpassword"):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        self.version = self.common.version()

    def get_course_ids(self):
        return self.models.execute_kw(self.db, self.uid, self.password, "elearning.course", "search", [[]],
                                      {"offset": 10, "limit": 5})

    def create(self, payload: dict):
        """Adds new record"""
        try:
            return self.models.execute_kw(
                self.db,
                self.uid,
                self.password,
                "elearning.course",
                "create",
                [
                    payload
                ],
            )
        except Exception as e:
            return f"{e}"

    def update(self, id: int, payload: dict):
        """Update record"""
        try:
            return self.models.execute_kw(
                self.db,
                self.uid,
                self.password,
                "elearning.course",
                "write",
                [
                    [id],
                    {
                       payload
                    },
                ],
            )
        except Exception as e:
            return f"{e}"
