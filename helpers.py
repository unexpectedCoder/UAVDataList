from numpy import ndarray, polyval, polyfit


def items_to_float(d: dict) -> dict:
    res = d.copy()
    for k in res.keys():
        if type(res[k]) == str:
            if is_digit(res[k]):
                res[k] = float(res[k])
    return res


def is_digit(s: str) -> bool:
    if s.isdigit():
        return True
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def get_poly(x: ndarray, y: ndarray, deg: int, new_x: ndarray) -> ndarray:
    return polyval(polyfit(x, y, deg), new_x)


def poly_val(coeffs: tuple, x: float) -> float:
    coeffs = coeffs[::-1]
    ans = 0
    for i, k in enumerate(coeffs):
        ans += k * x**i
    return ans
