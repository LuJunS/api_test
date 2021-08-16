from test.case.basecase import BaseCase


class TestCreateGroup(BaseCase):
    def test_create_Group_ture(self):
        case_data = self.get_case_data("test_create_Group_ture")
        self.send_request(case_data)