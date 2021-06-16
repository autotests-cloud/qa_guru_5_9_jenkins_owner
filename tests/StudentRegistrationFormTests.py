from faker import Faker
from selene import by, have, be
from selene import browser
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
        # @step("Open students registration form")
        @step
        def open_students_registration_form():
            open("https://demoqa.com/automation-practice-form")
            $(".practice-form-wrapper").shouldHave(text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            open("https://demoqa.com/automation-practice-form")

            @step("Fill common data")
            def _():
                $("#firstName").val(firstName)
                $("#lastName").val(lastName)
                $("#userEmail").val(email)
                $("#genterWrapper").$(byText(gender)).click()
                $("#userNumber").val(mobile)

            @step("Set date")
            def _():
                $("#dateOfBirthInput").clear()
                $(".react-datepicker__month-select").selectOption(monthOfBirth)
                $(".react-datepicker__year-select").selectOption(yearOfBirth)
                $(".react-datepicker__day--0" + dayOfBirth).click()

            @step("Set subjects")
            def _():
                $("#subjectsInput").val(subject1)
                $(".subjects-auto-complete__menu-list").$(byText(subject1)).click()
                $("#subjectsInput").val(subject2)
                $(".subjects-auto-complete__menu-list").$(byText(subject2)).click()

            @step("Set hobbies")
            def _():
                $("#hobbiesWrapper").$(byText(hobby1)).click()
                $("#hobbiesWrapper").$(byText(hobby2)).click()
                $("#hobbiesWrapper").$(byText(hobby3)).click()

            // TODO: consider refactor code like below for same style as everywhere else for consistency/easier reading
            /*
            @step("Upload image")
            def _():
                $("#uploadPicture").uploadFromClasspath("img/" + picture)

             */

            @step("Upload image")
            def _():
                $("#uploadPicture").uploadFromClasspath("img/" + picture)

            @step("Set address")
            def _():
                $("#currentAddress").val(currentAddress)
                $("#state").scrollTo().click()
                $("#stateCity-wrapper").$(byText(state)).click()
                $("#city").click()
                $("#stateCity-wrapper").$(byText(city)).click()

            @step("Submit form")
            def _():
                $("#submit").click()

        @step("Verify successful form submit")
        def _():
            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"))
            $x("//td[text()='Student Name']").parent().shouldHave(text(firstName + " " + lastName))
            $x("//td[text()='Student Email']").parent().shouldHave(text(email))
            $x("//td[text()='Gender']").parent().shouldHave(text(gender))
            $x("//td[text()='Mobile']").parent().shouldHave(text(mobile))
            $x("//td[text()='Date of Birth']").parent().shouldHave(text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
            $x("//td[text()='Subjects']").parent().shouldHave(text(subject1 + ", " + subject2))
            $x("//td[text()='Hobbies']").parent().shouldHave(text(hobby1 + ", " + hobby2 + ", " + hobby3))
            $x("//td[text()='Picture']").parent().shouldHave(text(picture))
            $x("//td[text()='Address']").parent().shouldHave(text(currentAddress))
            $x("//td[text()='State and City']").parent().shouldHave(text(state + " " + city))

    def test_negativeFillForm():
        @step("Open students registration form")
        def _():
            open("https://demoqa.com/automation-practice-form")
            $(".practice-form-wrapper").shouldHave(text("Student Registration Form"))

        @step("Fill students registration form")
        def _():
            @step("Fill common data")
            def _():
                $("#firstName").val(firstName)
                $("#lastName").val(lastName)
                $("#userEmail").val(email)
                $("#genterWrapper").$(byText(gender)).click()
                $("#userNumber").val(mobile)

            @step("Set date")
            def _():
                $("#dateOfBirthInput").clear()
                $(".react-datepicker__month-select").selectOption(monthOfBirth)
                $(".react-datepicker__year-select").selectOption(yearOfBirth)
                $(".react-datepicker__day--0" + dayOfBirth).click()

            @step("Set subjects")
            def _():
                $("#subjectsInput").val(subject1)
                $(".subjects-auto-complete__menu-list").$(byText(subject1)).click()
                $("#subjectsInput").val(subject2)
                $(".subjects-auto-complete__menu-list").$(byText(subject2)).click()

            @step("Set hobbies")
            def _():
                $("#hobbiesWrapper").$(byText(hobby1)).click()
                $("#hobbiesWrapper").$(byText(hobby2)).click()
                $("#hobbiesWrapper").$(byText(hobby3)).click()

            @step("Upload image")
            def _():
                $("#uploadPicture").uploadFromClasspath("img/" + picture))

            @step("Set address")
            def _():
                $("#currentAddress").val(currentAddress)
                $("#state").scrollTo().click()
                $("#stateCity-wrapper").$(byText(state)).click()
                $("#city").click()
                $("#stateCity-wrapper").$(byText(city)).click()

            @step("Submit form")
            def _():
                $("#submit").click()

        // TODO: refactor for cleaner test logic and less boilerplate ...
        @step("Verify successful form submit")
        def _():
            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"))
            $x("//td[text()='Student Name']").parent().shouldHave(text(firstName + " " + lastName))
            $x("//td[text()='Student Email']").parent().shouldHave(text(email))
            $x("//td[text()='Gender']").parent().shouldHave(text(gender))
            $x("//td[text()='Mobile']").parent().shouldHave(text(mobile))
            $x("//td[text()='Date of Birth']").parent().shouldHave(text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth))
            $x("//td[text()='Subjects']").parent().shouldHave(text(subject1 + ", " + subject2))
            $x("//td[text()='Hobbies']").parent().shouldHave(text(hobby1 + ", " + hobby2 + ", " + hobby3))
            $x("//td[text()='Picture']").parent().shouldHave(text(picture))
            $x("//td[text()='Address']").parent().shouldHave(text(currentAddress))
            $x("//td[text()='State and City']").parent().shouldHave(text(state + " error " + city))
