# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.account_es_normal_pyme.tests.test_account_es_normal_pyme import suite
except ImportError:
    from .test_account_es_normal_pyme import suite

__all__ = ['suite']
