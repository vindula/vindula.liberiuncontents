# -*- coding: utf-8 -*-
from five import grok

from vindula.liberiuncontents import MessageFactory as _

from AccessControl import ClassSecurityInfo

from vindula.liberiuncontents.content.interfaces import IPlanosPrecos
from Products.ATContentTypes.content.document import ATDocumentSchema,ATDocumentBase

from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.liberiuncontents.config import *
from DateTime.DateTime import DateTime
from time import strftime, gmtime


PlanosPrecos_schema = ATDocumentSchema.copy() + Schema((

    TextField(
            name='URLButton',
            widget=StringWidget(
                label=_(u"URL do destino."),
                description=_(u"Insira a URL que o usuário será direcionado ao clicar no botão de 'assinar'."),
                label_msgid='vindula_liberiuncontents_label_title_URLButton',
                description_msgid='vindula_liberiuncontents_title_URLButton',
                i18n_domain='vindula_liberiuncontents',
            ),
        required=True,
    ),
    
    TextField(
        name='textButton',
        widget=StringWidget(
            label=_(u"Texto do botão"),
            description=_(u"Insira o texto que aparecerá no botão."),
            label_msgid='vindula_liberiuncontents_label_textButton',
            description_msgid='vindula_liberiuncontents_help_textButton',
            i18n_domain='vindula_liberiuncontents',
        ),
        required=True,
        default='Inscrever-se'
    ),        

    TextField(
        name='textValor',
        widget=StringWidget(
            label=_(u"Texto destaque"),
            description=_(u"Texto que aparecerá acima do botão."),
            label_msgid='vindula_liberiuncontents_textValor',
            description_msgid='vindula_liberiuncontents_help_textValor',
            i18n_domain='vindula_liberiuncontents',
        ),
        required=False,
    ),   
    
    LinesField(
        name='featuresPlan',
        widget=InAndOutWidget(
            label=_(u"Funcionalidades do plano."),
            description=_(u"Selecione as funcionalidades presentes nessa versão."),
        ),
        vocabulary='getFeatures',
        required=True,
    ),
    
))

finalizeATCTSchema(PlanosPrecos_schema, folderish=False)

invisible = {'view':'invisible','edit':'invisible',}
#PlanosPrecos_schema['description'].widget.visible = invisible
PlanosPrecos_schema['text'].widget.visible = invisible

#Interface
class PlanosPrecos(ATDocumentBase):
    """ PlanosPrecos Page """
    
    security = ClassSecurityInfo()
    implements(IPlanosPrecos)    
    portal_type = 'PlanosPrecos'
    _at_rename_after_creation = True
    schema = PlanosPrecos_schema
    
    def getFeatures(self):
        L=[]
        dics = self.aq_parent.getFeatures()
        for dic in dics:
            L.append(dic['feature'])
        return L

registerType(PlanosPrecos, PROJECTNAME) 