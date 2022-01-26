/////////////////////////////////////////////////////////// #1# //////////////////////////////////////////////////////////////////////////////////////
// http://162.55.220.72:5005/first

// 1. Отправить запрос.
// 2. Статус код 200

pm.test("Status code  200", function () {
    pm.response.to.have.status(200);
});

// 3. Проверить, что в body приходит правильный string.

pm.test("Test string body", function () {
    pm.expect(pm.response.text()).to.include("This is the first responce from server!");
});

/////////////////////////////////////////////////////////// #2# //////////////////////////////////////////////////////////////////////////////////////
// http://162.55.220.72:5005/user_info_3
// 1. Отправить запрос.

// 2. Статус код 200
pm.test("Test | SC == 200", function () {
    pm.response.to.have.status(200);
});

// 3. Спарсить response body в json.
var resp = pm.response.json();

// 4. Проверить, что name в ответе равно name s request (name вбить руками.)
pm.test("Response | Name == Ilya", function () {
    pm.expect(resp.name).to.eql('Ilya');
});

// 5. Проверить, что age в ответе равно age s request (age вбить руками.)
var Age_1 = '24'
pm.test("Response | Age == 24", function () {
    pm.expect(resp.age).to.eql('24');
});

// 6. Проверить, что salary в ответе равно salary s request (salary вбить руками.)
pm.test("Response | Salary == 1000", function () {
    pm.expect(resp.salary).to.eql(1000);
});

// 7. Спарсить request.
var req = JSON.parse(responseBody);

// 8. Проверить, что name в ответе равно name s request (name забрать из request.)
pm.test("Response | Name == Ilya", function () {
    pm.expect(resp.name).to.eql(req.name);
});

// 9. Проверить, что age в ответе равно age s request (age забрать из request.)
pm.test("Response | Age == 24", function () {
    pm.expect(parseInt(resp.age)).to.eql(parseInt(req.age));
});

// 10. Проверить, что salary в ответе равно salary s request (salary забрать из request.)
pm.test("Response | Salary Check", function () {
    pm.expect(parseInt(resp.salary)).to.eql(req.salary);
});

// 11. Вывести в консоль параметр family из response.
console.log('resp.family == ', resp.family)

// 12. Проверить что u_salary_1_5_year в ответе равно salary*4 (salary забрать из request)
pm.test("Response | Salary * 4 == 4000", function () {
    pm.expect(resp.family.u_salary_1_5_year).to.eql(req.salary*4);
});

/////////////////////////////////////////////////////////// #3# //////////////////////////////////////////////////////////////////////////////////////

// http://162.55.220.72:5005/object_info_3
// 1. Отправить запрос.
// 2. Статус код 200
pm.test("Test | Status Code == 200", function () {
    pm.response.to.have.status(200);
});

// 3. Спарсить response body в json.
var resp = pm.response.json();

// 4. Спарсить request.
var req = pm.request.url.query.toObject();

// 5. Проверить, что name в ответе равно name s request (name забрать из request.)
pm.test("Response | Name Check", function () {
    pm.expect(resp.name).to.eql(req.name);
});

// 6. Проверить, что age в ответе равно age s request (age забрать из request.)
pm.test("Response | Age Check", function () {
    pm.expect(resp.age).to.eql(req.age);
});

// 7. Проверить, что salary в ответе равно salary s request (salary забрать из request.)
pm.test("Response | Salary Check", function () {
    pm.expect(resp.salary).to.eql(parseInt(req.salary));
});

// 8. Вывести в консоль параметр family из response.
console.log('resp.family == ', resp.family)

// 9. Проверить, что у параметра dog есть параметры name.
pm.test("Response | var DOG have var NAME", function () {    
    pm.expect(resp.family.pets.dog.name).to.exist;
})

// 10. Проверить, что у параметра dog есть параметры age.
pm.test("Response | var DOG have var AGE", function () {    
    pm.expect(resp.family.pets.dog.age).to.exist;
})

// 11. Проверить, что параметр name имеет значение Luky.
pm.test("Response | Check Dog Name", function () {
    pm.expect(resp.family.pets.dog.name).to.eql('Luky');
});

// 12. Проверить, что параметр age имеет значение 4.
pm.test("Response | Check Dog Age", function () {
    pm.expect(resp.family.pets.dog.age).to.eql(4);
});

/////////////////////////////////////////////////////////// #4# //////////////////////////////////////////////////////////////////////////////////////

// http://162.55.220.72:5005/object_info_4
// 1. Отправить запрос.
// 2. Статус код 200
pm.test("Test | Status Code = 200", function () {
    pm.response.to.have.status(200);
});

// 3. Спарсить response body в json.
var resp = pm.response.json();

// 4. Спарсить request.
var req = pm.request.url.query.toObject();

// 5. Проверить, что name в ответе равно name s request (name забрать из request.)
pm.test("Response | Name Check", function () {
    pm.expect(resp.name).to.eql(req.name);
});

// 6. Проверить, что age в ответе равно age из request (age забрать из request.)
pm.test("Response | Age Check", function () {
    pm.expect(resp.age).to.eql(parseInt(req.age));
});

// 7. Вывести в консоль параметр salary из request.
console.log('request =', req.salary)

// 8. Вывести в консоль параметр salary из response.
console.log('response =', resp.salary)

// 9. Вывести в консоль 0-й элемент параметра salary из response.
var salary_0 = resp.salary[0]
console.log('salary_0 =', salary_0)

// 10. Вывести в консоль 1-й элемент параметра salary параметр salary из response.
var salary_1 = resp.salary[1]
console.log('salary_1 =', salary_1)

// 11. Вывести в консоль 2-й элемент параметра salary параметр salary из response.
var salary_2 = resp.salary[2]
console.log('salary_2 =', salary_2)

// 12. Проверить, что 0-й элемент параметра salary равен salary из request (salary забрать из request.)
pm.test("Response | Salary[0] Check", function () {
    pm.expect(salary_0).to.eql(resp.salary[0]);
});

// 13. Проверить, что 1-й элемент параметра salary равен salary*2 из request (salary забрать из request.)
pm.test("Response | Salary[1] Check", function () {
    pm.expect(salary_1).to.eql(resp.salary[1]);
});

// 14. Проверить, что 2-й элемент параметра salary равен salary*3 из request (salary забрать из request.)
pm.test("Response | Salary[2] Check", function () {
    pm.expect(salary_2).to.eql(resp.salary[2]);
});

// 15. Создать в окружении переменную name
pm.environment.set("name")

// 16. Создать в окружении переменную age
pm.environment.set("age")

// 17. Создать в окружении переменную salary
pm.environment.set("salary")

// 18. Передать в окружение переменную name
pm.environment.set("name", 'Ilya')

// 19. Передать в окружение переменную age
pm.environment.set("age", 24)

// 20. Передать в окружение переменную salary
pm.environment.set("salary", 1000)

// 21. Написать цикл который выведет в консоль по порядку элементы списка из параметра salary.
var salary = resp.salary
var list = salary;
list.forEach(function(salary_item, index) {
    console.log('Список: ', salary_item);
});

/////////////////////////////////////////////////////////// #5# //////////////////////////////////////////////////////////////////////////////////////

// http://162.55.220.72:5005/user_info_2
// 1. Вставить параметр salary из окружения в request
// 2. Вставить параметр age из окружения в age
// 3. Вставить параметр name из окружения в name
// 4. Отправить запрос.
// 5. Статус код 200
pm.test("Test | Status Code = 200", function () {
    pm.response.to.have.status(200);
});

// 6. Спарсить response body в json.
var resp = pm.response.json();

// 7. Спарсить request.
var req = JSON.parse(responseBody);

// 8. Проверить, что json response имеет параметр start_qa_salary
pm.test("Response | Have var start_qa_salary", function () {    
    pm.expect(resp.start_qa_salary).to.exist;
})

// 9. Проверить, что json response имеет параметр qa_salary_after_6_months
pm.test("Response | Have var qa_salary_after_6_months", function () {    
    pm.expect(resp.qa_salary_after_6_months).to.exist;
})

// 10. Проверить, что json response имеет параметр qa_salary_after_12_months
pm.test("Response | Have var qa_salary_after_12_months", function () {    
    pm.expect(resp.qa_salary_after_12_months).to.exist;
})

// 11. Проверить, что json response имеет параметр qa_salary_after_1.5_year
pm.test("Response | Have var qa_salary_after_1.5_year", function () {    
    pm.expect(resp["qa_salary_after_1.5_year"]).to.exist;
})

// 12. Проверить, что json response имеет параметр qa_salary_after_3.5_years
pm.test("Response | Have var qa_salary_after_3.5_years", function () {    
    pm.expect(resp["qa_salary_after_3.5_years"]).to.exist;
})

// 13. Проверить, что json response имеет параметр person
pm.test("Response | Have var person", function () {    
    pm.expect(resp.person).to.exist;
})

// 14. Проверить, что параметр start_qa_salary равен salary из request (salary забрать из request.)
var u_name_0 = resp.person.u_name[0]
var u_name_1 = resp.person.u_name[1]
var u_name_2 = resp.person.u_name[2]
pm.test("Response | start_qa_salary == salary", function () {
    pm.expect(resp.start_qa_salary).to.eql(resp.person.u_name[1]);
});

// 15. Проверить, что параметр qa_salary_after_6_months равен salary*2 из request (salary забрать из request.)
pm.test("Response | qa_salary_after_6_months == salary*2", function () {
    pm.expect(resp.qa_salary_after_6_months).to.eql(resp.person.u_name[1]*2);
});

// 16. Проверить, что параметр qa_salary_after_12_months равен salary*2.7 из request (salary забрать из request.)
pm.test("Response | qa_salary_after_12_months == salary*2.7", function () {
    pm.expect(resp.qa_salary_after_12_months).to.eql(resp.person.u_name[1]*2.7);
});

// 17. Проверить, что параметр qa_salary_after_1.5_year равен salary*3.3 из request (salary забрать из request.)
pm.test("Response | qa_salary_after_1.5_year == salary*3.3", function () {
    pm.expect(resp["qa_salary_after_1.5_year"]).to.eql(resp.person.u_name[1]*3.3);
});

// 18. Проверить, что параметр qa_salary_after_3.5_years равен salary*3.8 из request (salary забрать из request.)
pm.test("Response | qa_salary_after_3.5_years == salary*3.8", function () {
    pm.expect(resp["qa_salary_after_3.5_years"]).to.eql(resp.person.u_name[1]*3.8);
});

// 19. Проверить, что в параметре person, 1-й элемент из u_name равен salary из request (salary забрать из request.)
pm.test("Response | u_name_1 == salary", function () {
    pm.expect(u_name_1).to.eql(parseInt(u_name_1));
});
console.log(req)

// 20. Проверить, что что параметр u_age равен age из request (age забрать из request.)
pm.test("Response | u_age == age", function () {
    pm.expect(resp.u_age).to.eql(req.age);
});

// 21. Проверить, что параметр u_salary_5_years равен salary*4.2 из request (salary забрать из request.)
pm.test("Response | u_salary_5_years == salary*4.2", function () {
    pm.expect(resp.person.u_salary_5_years).to.eql(u_name_1*4.2);
});

// 22. ***Написать цикл который выведет в консоль по порядку элементы списка из параметра person.
console.log(resp.person.u_age)
var salary = resp.person.u_name
var list = salary;
list.forEach(function(salary_item, index) {
    console.log(salary_item);
});
console.log(resp.person.u_salary_5_years)
