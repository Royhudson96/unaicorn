def fake_predict(user_age):
    if user_age > 10:
        prediction = "Survive(Over ten)"
    else:
        prediction = "Super Survive(Under ten)"
    return prediction