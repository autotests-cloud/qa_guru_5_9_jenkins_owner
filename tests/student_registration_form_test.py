from faker import Faker
from selene import by, have, be, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from python_web_ui_test.helpers.allure_reporting import step
from python_web_ui_test.model.components import Dropdown


faker = Faker()

firstName = faker.name().firstName()
lastName = faker.name().lastName()
email = faker.internet().emailAddress()
gender = "Other"
mobile = faker.number().digits(10)
dayOfBirth = "10"
monthOfBirth = "May"
yearOfBirth = "1988"
subject1 = "Chemistry"
subject2 = "Commerce"
hobby1 = "Sports"
hobby2 = "Reading"
hobby3 = "Music"
picture = "1.png"
currentAddress = faker.address().fullAddress()
state = "Uttar Pradesh"
city = "Merrut"


def test_successful_fill_form():
    @step("Open students registration form")
    def _():
        browser.open("https://demoqa.com/automation-practice-form")
        s(".practice-form-wrapper").should(have.text("Student Registration Form"))

    @step("Fill students registration form")
    def _():
        @step("Fill common data")
        def _():
            s("#firstName").set_value(firstName)
            s("#lastName").set_value(lastName)
            s("#userEmail").set_value(email)
            s("#genterWrapper").element(by.text(gender)).click()
            s("#userNumber").set_value(mobile)

        @step("Set date")
        def _():
            s("#dateOfBirthInput").clear()
            Dropdown(".react-datepicker__month-select").select(monthOfBirth)
            Dropdown(".react-datepicker__year-select").select(yearOfBirth)
            s(".react-datepicker__day--0" + dayOfBirth).click()

        @step("Set subjects")
        def _():
            s("#subjectsInput").set_value(subject1)
            s(".subjects-auto-complete__menu-list").element(by.text(subject1)).click()
            s("#subjectsInput").set_value(subject2)
            s(".subjects-auto-complete__menu-list").element(by.text(subject2)).click()

        @step("Set hobbies")
        def _():
            s("#hobbiesWrapper").element(by.text(hobby1)).click()
            s("#hobbiesWrapper").element(by.text(hobby2)).click()
            s("#hobbiesWrapper").element(by.text(hobby3)).click()

        @step("Upload image")
        def _():
            s("#uploadPicture").type("resources/img/" + picture)

        @step("Set address")
        def _():
            s("#currentAddress").set_value(currentAddress)
            s("#state").perform(command.js.scroll_into_view).click()
            s("#stateCity-wrapper").element(by.text(state)).click()
            s("#city").click()
            s("#stateCity-wrapper").element(by.text(city)).click()

        @step("Submit form")
        def _():
            s("#submit").click()

    @step("Verify successful form submit")
    def _():
        s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        s("//td[text()='Student Name']").element("..").should(have.text(firstName + " " + lastName))
        s("//td[text()='Student Email']").element("..").should(have.text(email))
        s("//td[text()='Gender']").element("..").should(have.text(gender))
        s("//td[text()='Mobile']").element("..").should(have.text(mobile))
        s("//td[text()='Date of Birth']").element("..").should(have.text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
        s("//td[text()='Subjects']").element("..").should(have.text(subject1 + ", " + subject2))
        s("//td[text()='Hobbies']").element("..").should(have.text(hobby1 + ", " + hobby2 + ", " + hobby3))
        s("//td[text()='Picture']").element("..").should(have.text(picture))
        s("//td[text()='Address']").element("..").should(have.text(currentAddress))
        s("//td[text()='State and City']").element("..").should(have.text(state + " " + city))


def test_negative_fill_form():
    @step("Open students registration form")
    def _():
        browser.open("https://demoqa.com/automation-practice-form")
        s(".practice-form-wrapper").should(have.text("Student Registration Form"))

    @step("Fill students registration form")
    def _():
        @step("Fill common data")
        def _():
            s("#firstName").set_value(firstName)
            s("#lastName").set_value(lastName)
            s("#userEmail").set_value(email)
            s("#genterWrapper").element(by.text(gender)).click()
            s("#userNumber").set_value(mobile)

        @step("Set date")
        def _():
            s("#dateOfBirthInput").clear()
            Dropdown(".react-datepicker__month-select").select(monthOfBirth)
            Dropdown(".react-datepicker__year-select").select(yearOfBirth)
            s(".react-datepicker__day--0" + dayOfBirth).click()

        @step("Set subjects")
        def _():
            s("#subjectsInput").set_value(subject1)
            s(".subjects-auto-complete__menu-list").element(by.text(subject1)).click()
            s("#subjectsInput").set_value(subject2)
            s(".subjects-auto-complete__menu-list").element(by.text(subject2)).click()

        @step("Set hobbies")
        def _():
            s("#hobbiesWrapper").element(by.text(hobby1)).click()
            s("#hobbiesWrapper").element(by.text(hobby2)).click()
            s("#hobbiesWrapper").element(by.text(hobby3)).click()

        @step("Upload image")
        def _():
            s("#uploadPicture").type("resources/img/" + picture)

        @step("Set address")
        def _():
            s("#currentAddress").set_value(currentAddress)
            s("#state").perform(command.js.scroll_into_view).click()
            s("#stateCity-wrapper").element(by.text(state)).click()
            s("#city").click()
            s("#stateCity-wrapper").element(by.text(city)).click()

        @step("Submit form")
        def _():
            s("#submit").click()

    # TODO: refactor for cleaner test logic and less boilerplate ...
    @step("Verify successful form submit")
    def _():
        s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        s("//td[text()='Student Name']").element("..").should(have.text(firstName + " " + lastName))
        s("//td[text()='Student Email']").element("..").should(have.text(email))
        s("//td[text()='Gender']").element("..").should(have.text(gender))
        s("//td[text()='Mobile']").element("..").should(have.text(mobile))
        s("//td[text()='Date of Birth']").element("..").should(have.text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
        s("//td[text()='Subjects']").element("..").should(have.text(subject1 + ", " + subject2))
        s("//td[text()='Hobbies']").element("..").should(have.text(hobby1 + ", " + hobby2 + ", " + hobby3))
        s("//td[text()='Picture']").element("..").should(have.text(picture))
        s("//td[text()='Address']").element("..").should(have.text(currentAddress))
        s("//td[text()='State and City']").element("..").should(have.text(state + " error " + city))
