from accounts.models import Account, Profile
from django.contrib.auth.models import User
from django.db import transaction
from accounts.models import Account, Profile


def sign_up_user(**kwargs):
    fname = kwargs.get(fname)
    lname = kwargs.get(lname)
    username = kwargs.get(username)
    password = kwargs.get(password)
    business_name = kwargs.get(business_name)

    with transaction.atomic():
        account = Account.objects.create(
            name=business_name
        )
        account.save()

        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=username
        )
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(
            user=user,
            account=account,
            is_business_owner=True
        )
        profile.save()
    return user


def user_edit(user_id, **kwargs):
    user = User.objects.get(pk=user_id)
    user.first_name = kwargs.get('first_name')
    user.last_name = kwargs.get('last_name')
    user.username = kwargs.get('username')
    user.email = kwargs.get('email')
    user.save()
    return user


def account_edit(account_id, **kwargs):
    account = Account.objects.get(pk=account_id)
    account.name = kwargs.get('name')
    account.save()
    return account

