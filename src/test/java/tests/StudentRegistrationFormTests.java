package tests;

import com.github.javafaker.Faker;
import org.junit.jupiter.api.Test;

import static com.codeborne.selenide.Condition.text;
import static com.codeborne.selenide.Selectors.byText;
import static com.codeborne.selenide.Selenide.*;
import static io.qameta.allure.Allure.step;

public class StudentRegistrationFormTests extends ConfTest {

    Faker faker = new Faker();

    String firstName = faker.name().firstName(),
            lastName = faker.name().lastName(),
            email = faker.internet().emailAddress(),
            gender = "Other", // it's more a selector than test data... TODO: move to the test itself for consistency with other selectors, where we don't use variables/fields for DRY
            mobile = faker.number().digits(10),
            dayOfBirth = "10",
            monthOfBirth = "May",
            yearOfBirth = "1988",
            subject1 = "Chemistry",
            subject2 = "Commerce",
            hobby1 = "Sports",  // it's more a selector than test data... TODO: move to the test itself for consistency with other selectors, where we don't use variables/fields for DRY
            hobby2 = "Reading",  // it's more a selector than test data... TODO: move to the test itself for consistency with other selectors, where we don't use variables/fields for DRY
            hobby3 = "Music",  // it's more a selector than test data... TODO: move to the test itself for consistency with other selectors, where we don't use variables/fields for DRY
            picture = "1.png",
            currentAddress = faker.address().fullAddress(),
            state = "Uttar Pradesh",
            city = "Merrut";

    @Test
    void successfulFillFormTest() {
        step("Open students registration form", () -> {
            open("https://demoqa.com/automation-practice-form");
            $(".practice-form-wrapper").shouldHave(text("Student Registration Form"));
        });

        step("Fill students registration form", () -> {
            step("Fill common data", () -> {
                $("#firstName").val(firstName); // kind of tight coupling to test data...
                $("#lastName").val(lastName);
                $("#userEmail").val(email);
                $("#genterWrapper").$(byText(gender)).click(); // might be not stable/economic enough when searching by text
                $("#userNumber").val(mobile);
            });
            step("Set date", () -> {
                $("#dateOfBirthInput").clear();
                $(".react-datepicker__month-select").selectOption(monthOfBirth);
                $(".react-datepicker__year-select").selectOption(yearOfBirth);
                $(".react-datepicker__day--0" + dayOfBirth).click();
            });
            step("Set subjects", () -> {
                $("#subjectsInput").val(subject1);
                $(".subjects-auto-complete__menu-list").$(byText(subject1)).click();
                $("#subjectsInput").val(subject2);
                $(".subjects-auto-complete__menu-list").$(byText(subject2)).click();
            });
            step("Set hobbies", () -> {
                $("#hobbiesWrapper").$(byText(hobby1)).click();
                $("#hobbiesWrapper").$(byText(hobby2)).click();
                $("#hobbiesWrapper").$(byText(hobby3)).click();
            });
            // TODO: consider refactor code like below for same style as everywhere else for consistency/easier reading
            /*
            step("Upload image", () -> {
                $("#uploadPicture").uploadFromClasspath("img/" + picture)
            });
             */
            step("Upload image", () ->
                    $("#uploadPicture").uploadFromClasspath("img/" + picture));
            step("Set address", () -> {
                $("#currentAddress").val(currentAddress);
                $("#state").scrollTo().click();
                $("#stateCity-wrapper").$(byText(state)).click();
                $("#city").click();
                $("#stateCity-wrapper").$(byText(city)).click();
            });
            step("Submit form", () ->
                $("#submit").click());
        });

        step("Verify successful form submit", () -> {
            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"));
            $x("//td[text()='Student Name']").parent().shouldHave(text(firstName + " " + lastName));
            $x("//td[text()='Student Email']").parent().shouldHave(text(email));
            $x("//td[text()='Gender']").parent().shouldHave(text(gender));
            $x("//td[text()='Mobile']").parent().shouldHave(text(mobile));
            $x("//td[text()='Date of Birth']").parent().shouldHave(text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth));
            $x("//td[text()='Subjects']").parent().shouldHave(text(subject1 + ", " + subject2));
            $x("//td[text()='Hobbies']").parent().shouldHave(text(hobby1 + ", " + hobby2 + ", " + hobby3));
            $x("//td[text()='Picture']").parent().shouldHave(text(picture));
            $x("//td[text()='Address']").parent().shouldHave(text(currentAddress));
            $x("//td[text()='State and City']").parent().shouldHave(text(state + " " + city));
        });
    }

    @Test
    void negativeFillFormTest() {
        step("Open students registration form", () -> {
            open("https://demoqa.com/automation-practice-form");
            $(".practice-form-wrapper").shouldHave(text("Student Registration Form"));
        });

        step("Fill students registration form", () -> {
            step("Fill common data", () -> {
                $("#firstName").val(firstName);
                $("#lastName").val(lastName);
                $("#userEmail").val(email);
                $("#genterWrapper").$(byText(gender)).click();
                $("#userNumber").val(mobile);
            });
            step("Set date", () -> {
                $("#dateOfBirthInput").clear();
                $(".react-datepicker__month-select").selectOption(monthOfBirth);
                $(".react-datepicker__year-select").selectOption(yearOfBirth);
                $(".react-datepicker__day--0" + dayOfBirth).click();
            });
            step("Set subjects", () -> {
                $("#subjectsInput").val(subject1);
                $(".subjects-auto-complete__menu-list").$(byText(subject1)).click();
                $("#subjectsInput").val(subject2);
                $(".subjects-auto-complete__menu-list").$(byText(subject2)).click();
            });
            step("Set hobbies", () -> {
                $("#hobbiesWrapper").$(byText(hobby1)).click();
                $("#hobbiesWrapper").$(byText(hobby2)).click();
                $("#hobbiesWrapper").$(byText(hobby3)).click();
            });
            step("Upload image", () ->
                    $("#uploadPicture").uploadFromClasspath("img/" + picture));
            step("Set address", () -> {
                $("#currentAddress").val(currentAddress);
                $("#state").scrollTo().click();
                $("#stateCity-wrapper").$(byText(state)).click();
                $("#city").click();
                $("#stateCity-wrapper").$(byText(city)).click();
            });
            step("Submit form", () ->
                    $("#submit").click());
        });

        // TODO: refactor for cleaner test logic and less boilerplate ...
        step("Verify successful form submit", () -> {
            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"));
            $x("//td[text()='Student Name']").parent().shouldHave(text(firstName + " " + lastName));
            $x("//td[text()='Student Email']").parent().shouldHave(text(email));
            $x("//td[text()='Gender']").parent().shouldHave(text(gender));
            $x("//td[text()='Mobile']").parent().shouldHave(text(mobile));
            $x("//td[text()='Date of Birth']").parent().shouldHave(text(dayOfBirth + " " + monthOfBirth + "," + yearOfBirth));
            $x("//td[text()='Subjects']").parent().shouldHave(text(subject1 + ", " + subject2));
            $x("//td[text()='Hobbies']").parent().shouldHave(text(hobby1 + ", " + hobby2 + ", " + hobby3));
            $x("//td[text()='Picture']").parent().shouldHave(text(picture));
            $x("//td[text()='Address']").parent().shouldHave(text(currentAddress));
            $x("//td[text()='State and City']").parent().shouldHave(text(state + " error " + city));
        });
//        // TODO: ... either option 1 with page object for table component:
//        step("Verify successful form submit", () -> {
//            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"));
//            table(".modal-content").shouldHave(new String[][]{
//                    {"Student Name", firstName + " " + lastName},
//                    {"Student Email", email},
//                    {"Gender", gender},
//                    {"Mobile", mobile},
//                    {"Date of Birth", dayOfBirth + " " + monthOfBirth + "," + yearOfBirth},
//                    {"Subjects", subject1 + ", " + subject2},
//                    {"Hobbies", hobby1 + ", " + hobby2 + ", " + hobby3},
//                    {"Picture", picture},
//                    {"Address", currentAddress},
//                    {"State and City", state + " error " + city},
//            });
//        });
//
//        // TODO: ... or option 2 with custom selenide condition:
//        step("Verify successful form submit", () -> {
//            $("#example-modal-sizes-title-lg").shouldHave(text("Thanks for submitting the form"));
//            $(".modal-content").shouldHave(tableData(new String[][]{
//                    {"Student Name", firstName + " " + lastName},
//                    {"Student Email", email},
//                    {"Gender", gender},
//                    {"Mobile", mobile},
//                    {"Date of Birth", dayOfBirth + " " + monthOfBirth + "," + yearOfBirth},
//                    {"Subjects", subject1 + ", " + subject2},
//                    {"Hobbies", hobby1 + ", " + hobby2 + ", " + hobby3},
//                    {"Picture", picture},
//                    {"Address", currentAddress},
//                    {"State and City", state + " error " + city},
//            }));
//        });
    }
}