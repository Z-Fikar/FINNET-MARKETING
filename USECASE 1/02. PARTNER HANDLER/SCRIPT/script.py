import sys


def main() -> str:
    return sys.executable


def get_captcha(file_path: str) -> str:
    from anticaptchaofficial.imagecaptcha import imagecaptcha

    CAPTCHA_API_KEY = "a9b49ae349abda8eac65595bc26c853e"
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(CAPTCHA_API_KEY)

    # Specify softId to earn 10% commission with your app.
    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)

    # optional parameters, see documentation for details
    # 2 words
    # solver.set_phrase(True)
    # case sensitivity
    solver.set_case(True)
    # only numbers
    # solver.set_numeric(1)
    # minimum captcha text length
    solver.set_minLength(6)
    # maximum captcha text length
    # solver.set_maxLength(10)
    # math operation result, for captchas with text like 50+5
    # solver.set_math(True)
    # comment for workers
    # solver.set_comment("only green characters")
    # language pool
    # solver.set_language_pool("en")
    captcha_text = solver.solve_and_return_solution(file_path)
    result = ""
    if captcha_text != 0:
        result = captcha_text
        # print("captcha text "+captcha_text)
    # else:
        # print("task finished with error "+solver.error_code)
    return result


if __name__ == "__main__":
    # user defined test code, will not be called by Cyclone
    print("main", main())
    file_path = r"\\192.168.144.88\rpa\Use Case 2\Captcha\2025-03-05 09-41-09.jpg "
    print("get_captcha", get_captcha(file_path))
