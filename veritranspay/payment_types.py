from . import mixins


class PaymentTypeBase(mixins.SerializableMixin):
    '''
    Base type for all payment types.  Not usable by itself.
    '''
    def serialize(self):
        return {"payment_type": self.PAYMENT_TYPE_KEY,
                self.PAYMENT_TYPE_KEY: {},
                }


class CreditCard(PaymentTypeBase):
    '''
    A payment made with a credit card.
    http://docs.veritranspay.co.id/sandbox/charge.html#vtdirect-cc
    '''
    PAYMENT_TYPE_KEY = 'credit_card'

    def __init__(self, bank, token_id):
        '''
        :param bank: Represents the acquiring bank.
        :type bank: :py:class:`str`
        :param token_id: A token retrieved from the Veritrans
            JavaScript library, after submitting the credit card details.
        :type token_id: :py:class:`str`
        '''
        self.bank = bank
        self.token_id = token_id

    def serialize(self):
        rv = super(CreditCard, self).serialize()
        rv[self.PAYMENT_TYPE_KEY] = {'bank': self.bank,
                                     'token_id': self.token_id,
                                     }
        return rv

#
# NOTE:
# The following types are not yet supported!
# They will be added to the documentation as support is added
#

class MandiriClickpay(PaymentTypeBase):
    # http://docs.veritranspay.co.id/sandbox/charge.html#vtdirect-mandiri
    PAYMENT_TYPE_KEY = 'mandiri_clickpay'

    def __init__(self, card_number, input1, input2, input3):
        raise NotImplementedError("Only CreditCard is implemented.")

class CimbClicks(PaymentTypeBase):
    # http://docs.veritranspay.co.id/sandbox/charge.html#vtdirect-cimb
    PAYMENT_TYPE_KEY = 'cimb_clicks'

    def __init__(self, description):
        raise NotImplementedError("Only CreditCard is implemented.")
