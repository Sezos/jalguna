from odoo import models, fields, api

class jalguna(models.Model):
    _name = 'jalguna'
    _description = 'jalguna'
    neravna = fields.Char()
    nasavna = fields.Integer()
    mergejilavna = fields.Char()
    udurtsagavna = fields.Datetime() 
    irtsagavna = fields.Datetime() 
    yvtsagavna = fields.Datetime()