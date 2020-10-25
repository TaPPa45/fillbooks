# coding=utf-8
from django import template
from main.models import GoodsBrand, Branch
from main.const import *
from accounts.models import Branch

register = template.Library()

@register.simple_tag(takes_context=False)
def get_brands():
    return GoodsBrand.objects.all().values('name', 'pk')
    
@register.simple_tag(takes_context=False)
def get_status():
    statuses = [GOOD_STATUS_AWAIT, GOOD_STATUS_REJECT, GOOD_STATUS_PURCHASE, GOOD_STATUS_PRICED]
    return statuses

@register.simple_tag(takes_context=False)
def get_branchs():
    return Branch.objects.all().values('name', 'pk')