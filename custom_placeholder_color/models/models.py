# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_placeholder_color(models.Model):
#     _name = 'custom_placeholder_color.custom_placeholder_color'
#     _description = 'custom_placeholder_color.custom_placeholder_color'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
