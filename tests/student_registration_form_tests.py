import os

from faker import Faker

from selene import have, be, by, command
from selene.support.shared import browser
from python_web_test_kit.helpers.reporting import step
from selene.support.shared.jquery_style import s

from python_web_test_kit.model.controls import DropDown


class TestStudentRegistrationForm:
    faker = Faker()

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    gender = "Other"
    mobile = str(faker.random_number(digits=10))
    day_of_birth = "10"
    month_of_birth = "May"
    year_of_birth = "1988"
    subject1 = "Chemistry"
    subject2 = "Commerce"
    hobby1 = "Sports"
    hobby2 = "Reading"
    hobby3 = "Music"
    picture = "1.png"
    current_address = faker.street_address()
    state = "Uttar Pradesh"
    city = "Merrut"

    def test_successful_fill_form_test(self):
        @step("Open students registration form")
        def _():
            browser.open("/automation-practice-form")
            s(".practice-form-wrapper").should(have.text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            @step("Fill common data")
            def _():
                s("#firstName").set_value(self.first_name)
                s("#lastName").set_value(self.last_name)
                s("#userEmail").set_value(self.email)
                s("#genterWrapper").s(by.text(self.gender)).click()
                s("#userNumber").set_value(self.mobile)

            @step("Set date")
            def _():
                s("#dateOfBirthInput").clear()
                DropDown(".react-datepicker__month-select").select(self.month_of_birth)
                DropDown(".react-datepicker__year-select").select(self.year_of_birth)
                s(".react-datepicker__day--0" + self.day_of_birth).click()

            @step("Set subjects")
            def _():
                s("#subjectsInput").set_value(self.subject1)
                s(".subjects-auto-complete__menu-list").s(by.text(self.subject1)).click()
                s("#subjectsInput").set_value(self.subject2)
                s(".subjects-auto-complete__menu-list").s(by.text(self.subject2)).click()

            @step("Set hobbies")
            def _():
                s("#hobbiesWrapper").s(by.text(self.hobby1)).click()
                s("#hobbiesWrapper").s(by.text(self.hobby2)).click()
                s("#hobbiesWrapper").s(by.text(self.hobby3)).click()

            @step("Upload image")
            def _():
                s("#uploadPicture").type(os.path.abspath("../resources/img/" + self.picture))

            @step("Set address")
            def _():
                s("#currentAddress").set_value(self.current_address)
                s("#state").perform(command.js.scroll_into_view).click()
                s("#stateCity-wrapper").s(by.text(self.state)).click()
                s("#city").click()
                s("#stateCity-wrapper").s(by.text(self.city)).click()

            @step("Submit form")
            def _():
                s("#submit").click()

        @step("Verify successful form submit")
        def _():
            s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
            s("//td[text()='Student Name']").s("..").should(have.text(self.first_name + " " + self.last_name))
            s("//td[text()='Student Email']").s("..").should(have.text(self.email))
            s("//td[text()='Gender']").s("..").should(have.text(self.gender))
            s("//td[text()='Mobile']").s("..").should(have.text(self.mobile))
            s("//td[text()='Date of Birth']").s("..").should(
                have.text(self.day_of_birth + " " + self.month_of_birth + "," + self.year_of_birth))
            s("//td[text()='Subjects']").s("..").should(have.text(self.subject1 + ", " + self.subject2))
            s("//td[text()='Hobbies']").s("..").should(have.text(self.hobby1 + ", " + self.hobby2 + ", " + self.hobby3))
            s("//td[text()='Picture']").s("..").should(have.text(self.picture))
            s("//td[text()='Address']").s("..").should(have.text(self.current_address))
            s("//td[text()='State and City']").s("..").should(have.text(self.state + " " + self.city))

    def test_negative_fill_form_test(self):
        @step("Open students registration form")
        def _():
            browser.open("/automation-practice-form")
            s(".practice-form-wrapper").should(have.text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            @step("Fill common data")
            def _():
                s("#firstName").set_value(self.first_name)
                s("#lastName").set_value(self.last_name)
                s("#userEmail").set_value(self.email)
                s("#genterWrapper").s(by.text(self.gender)).click()
                s("#userNumber").set_value(self.mobile)

            @step("Set date")
            def _():
                s("#dateOfBirthInput").clear()
                DropDown(".react-datepicker__month-select").select(self.month_of_birth)
                DropDown(".react-datepicker__year-select").select(self.year_of_birth)
                s(".react-datepicker__day--0" + self.day_of_birth).click()

            @step("Set subjects")
            def _():
                s("#subjectsInput").set_value(self.subject1)
                s(".subjects-auto-complete__menu-list").s(by.text(self.subject1)).click()
                s("#subjectsInput").set_value(self.subject2)
                s(".subjects-auto-complete__menu-list").s(by.text(self.subject2)).click()

            @step("Set hobbies")
            def _():
                s("#hobbiesWrapper").s(by.text(self.hobby1)).click()
                s("#hobbiesWrapper").s(by.text(self.hobby2)).click()
                s("#hobbiesWrapper").s(by.text(self.hobby3)).click()

            @step("Upload image")
            def _():
                s("#uploadPicture").type(os.path.abspath("../resources/img/" + self.picture))

            @step("Set address")
            def _():
                s("#currentAddress").set_value(self.current_address)
                s("#state").perform(command.js.scroll_into_view).click()
                s("#stateCity-wrapper").s(by.text(self.state)).click()
                s("#city").click()
                s("#stateCity-wrapper").s(by.text(self.city)).click()

            @step("Submit form")
            def _():
                s("#submit").click()

        @step("Verify successful form submit")
        def _():
            s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
            s("//td[text()='Student Name']").s("..").should(have.text(self.first_name + " " + self.last_name))
            s("//td[text()='Student Email']").s("..").should(have.text(self.email))
            s("//td[text()='Gender']").s("..").should(have.text(self.gender))
            s("//td[text()='Mobile']").s("..").should(have.text(self.mobile))
            s("//td[text()='Date of Birth']").s("..").should(
                have.text(self.day_of_birth + " " + self.month_of_birth + "," + self.year_of_birth))
            s("//td[text()='Subjects']").s("..").should(have.text(self.subject1 + ", " + self.subject2))
            s("//td[text()='Hobbies']").s("..").should(have.text(self.hobby1 + ", " + self.hobby2 + ", " + self.hobby3))
            s("//td[text()='Picture']").s("..").should(have.text(self.picture))
            s("//td[text()='Address']").s("..").should(have.text(self.current_address))
            s("//td[text()='State and City']").s("..").should(have.text(self.state + " error " + self.city))