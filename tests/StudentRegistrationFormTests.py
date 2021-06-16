from faker import Faker
from selene import by, have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from python_web_ui_test.helpers.allure_reporting import step

class StudentRegistrationFormTests:

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

    def test_successfulFillForm():
        @step("Open students registration form")
        def _():
            browser.open("https://demoqa.com/automation-practice-form")
            s(".practice-form-wrapper").should(have.text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            @step("Fill common data")
            def _():
                s("#firstName").val(firstName)
                s("#lastName").val(lastName)
                s("#userEmail").val(email)
                s("#genterWrapper").element(byText(gender)).click()
                s("#userNumber").val(mobile)

            @step("Set date")
            def _():
                s("#dateOfBirthInput").clear()
                s(".react-datepicker__month-select").selectOption(monthOfBirth)
                s(".react-datepicker__year-select").selectOption(yearOfBirth)
                s(".react-datepicker__day--0" + dayOfBirth).click()

            @step("Set subjects")
            def _():
                s("#subjectsInput").val(subject1)
                s(".subjects-auto-complete__menu-list").element(byText(subject1)).click()
                s("#subjectsInput").val(subject2)
                s(".subjects-auto-complete__menu-list").element(byText(subject2)).click()

            @step("Set hobbies")
            def _():
                s("#hobbiesWrapper").element(byText(hobby1)).click()
                s("#hobbiesWrapper").element(byText(hobby2)).click()
                s("#hobbiesWrapper").element(byText(hobby3)).click()

            @step("Upload image")
            def _():
                s("#uploadPicture").uploadFromClasspath("img/" + picture)

            @step("Set address")
            def _():
                s("#currentAddress").val(currentAddress)
                s("#state").scrollTo().click()
                s("#stateCity-wrapper").element(byText(state)).click()
                s("#city").click()
                s("#stateCity-wrapper").element(byText(city)).click()

            @step("Submit form")
            def _():
                s("#submit").click()

        @step("Verify successful form submit")
        def _():
            s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
            s("//td[text()='Student Name']").parent().should(have.text(firstName + " " + lastName))
            s("//td[text()='Student Email']").parent().should(have.text(email))
            s("//td[text()='Gender']").parent().should(have.text(gender))
            s("//td[text()='Mobile']").parent().should(have.text(mobile))
            s("//td[text()='Date of Birth']").parent().should(have.text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
            s("//td[text()='Subjects']").parent().should(have.text(subject1 + ", " + subject2))
            s("//td[text()='Hobbies']").parent().should(have.text(hobby1 + ", " + hobby2 + ", " + hobby3))
            s("//td[text()='Picture']").parent().should(have.text(picture))
            s("//td[text()='Address']").parent().should(have.text(currentAddress))
            s("//td[text()='State and City']").parent().should(have.text(state + " " + city))

    def test_negativeFillForm():
        @step("Open students registration form")
        def _():
            browser.open("https://demoqa.com/automation-practice-form")
            s(".practice-form-wrapper").should(have.text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            @step("Fill common data")
            def _():
                s("#firstName").val(firstName)
                s("#lastName").val(lastName)
                s("#userEmail").val(email)
                s("#genterWrapper").element(byText(gender)).click()
                s("#userNumber").val(mobile)

            @step("Set date")
            def _():
                s("#dateOfBirthInput").clear()
                s(".react-datepicker__month-select").selectOption(monthOfBirth)
                s(".react-datepicker__year-select").selectOption(yearOfBirth)
                s(".react-datepicker__day--0" + dayOfBirth).click()

            @step("Set subjects")
            def _():
                s("#subjectsInput").val(subject1)
                s(".subjects-auto-complete__menu-list").element(byText(subject1)).click()
                s("#subjectsInput").val(subject2)
                s(".subjects-auto-complete__menu-list").element(byText(subject2)).click()

            @step("Set hobbies")
            def _():
                s("#hobbiesWrapper").element(byText(hobby1)).click()
                s("#hobbiesWrapper").element(byText(hobby2)).click()
                s("#hobbiesWrapper").element(byText(hobby3)).click()

            @step("Upload image")
            def _():
                s("#uploadPicture").uploadFromClasspath("img/" + picture))

            @step("Set address")
            def _():
                s("#currentAddress").val(currentAddress)
                s("#state").scrollTo().click()
                s("#stateCity-wrapper").element(byText(state)).click()
                s("#city").click()
                s("#stateCity-wrapper").element(byText(city)).click()

            @step("Submit form")
            def _():
                s("#submit").click()

        # TODO: refactor for cleaner test logic and less boilerplate ...
        @step("Verify successful form submit")
        def _():
            s("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
            s("//td[text()='Student Name']").parent().should(have.text(firstName + " " + lastName))
            s("//td[text()='Student Email']").parent().should(have.text(email))
            s("//td[text()='Gender']").parent().should(have.text(gender))
            s("//td[text()='Mobile']").parent().should(have.text(mobile))
            s("//td[text()='Date of Birth']").parent().should(have.text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
            s("//td[text()='Subjects']").parent().should(have.text(subject1 + ", " + subject2))
            s("//td[text()='Hobbies']").parent().should(have.text(hobby1 + ", " + hobby2 + ", " + hobby3))
            s("//td[text()='Picture']").parent().should(have.text(picture))
            s("//td[text()='Address']").parent().should(have.text(currentAddress))
            s("//td[text()='State and City']").parent().should(have.text(state + " error " + city))
