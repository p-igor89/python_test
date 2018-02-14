def test_del_first_group(app):
    app.session.login("secret", "admin")
    app.group.del_first_group()
    app.session.logout()
