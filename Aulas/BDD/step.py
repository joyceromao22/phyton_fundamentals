from behave import step


@step('soma"{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma =  soma(int(num1), int(nu2))

    