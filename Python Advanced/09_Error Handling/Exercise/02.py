VALID_DOMAINS = [".com", ".bg", ".org", ".net"]


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def short_name(string):
    if len(string) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def not_containing_symbol(symbol, string):
    if symbol not in string:
        raise MustContainAtSymbolError("Email must contain @")


def get_tld(domain):
    return f".{domain.split('.')[-1]}"


def invalid_domain(domain, list):
    tld = get_tld(domain)
    if tld not in list:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


while True:
    line = input()
    if line == "End":
        break
    email = line

    not_containing_symbol("@", email)

    name, domain = email.split("@")

    short_name(name)
    invalid_domain(domain, VALID_DOMAINS)

    print("Email is valid")
