##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# ~ 'external_dependencies': {'python': ['swedbankpay']},
##############################################################################
{
        'name': 'SwedbankPay Payment Acquirer',
        'version': "14.0.1.0.0",
        'summary': 'Payment Acquirer: Swedbank Pay Implementation',
        'category': 'Hidden',
        'description': """SwedbankPay Payment Acquirer.""",
        'author': 'Vertel AB',
    'license': 'AGPL-3',
        'website': 'http://www.vertel.se',
        'depends': ['payment',
                    'account_payment'],
        'data': ['views/swedbankpay.xml',
                 'views/payment_acquirer.xml',
                 'data/swedbankpay_data.xml',
                 'views/res_cnfig_view.xml',
                 ],
        'installable': True,
}
