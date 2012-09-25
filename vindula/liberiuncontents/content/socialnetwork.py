# -*- coding: utf-8 -*-
from zope.interface import implements

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from AccessControl import ClassSecurityInfo

from vindula.liberiuncontents.config import *
from vindula.liberiuncontents import MessageFactory as _
from vindula.liberiuncontents.content.interfaces import ISocialNetwork
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

# Interface and schema
SocialNetwork_schema = schemata.ATContentTypeSchema.copy() + Schema((
                                                                     
    ReferenceField('image',
        multiValued=0,
        allowed_types=('Image',),
        relationship='image_banner',
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Imagem"),
            description=_(u"Insira uma imagem, ícone ou logo que faça referência à rede social."),
            
            label_msgid='vindula_liberiuncontents_label_image',
            description_msgid='vindula_liberiuncontents_help_image',
            i18n_domain='vindula_liberiuncontents',
            ),
        required=True
    ),
    
    IntegerField(
        name='imageWidth',
        widget=IntegerWidget(
            label=_(u"Largura da imagem"),
            description=_(u"Largura da imagem em pixels, insira apenas números inteiros."),
            
            label_msgid='vindula_liberiuncontents_label_imageWidth',
            description_msgid='vindula_liberiuncontents_help_imageWidth',
            i18n_domain='vindula_liberiuncontents',
        ),
        default=32,
        required=True
    ),
    
    IntegerField(
        name='imageHeight',
        widget=IntegerWidget(
            label=_(u"Altura da imagem"),
            description=_(u"Altura da imagem em pixels, insira apenas números inteiros."),
            
            label_msgid='vindula_liberiuncontents_label_imageHeight',
            description_msgid='vindula_liberiuncontents_help_imageHeight',
            i18n_domain='vindula_liberiuncontents',
        ),
        default=32,
        required=True
    ),
    
    TextField(
            name='link',
            widget=StringWidget(
                label=_(u"Link"),
                description=_(u"Insira a URL de destino do link."),
                label_msgid='vindula_liberiuncontents_label_link',
                description_msgid='vindula_liberiuncontents_link',
                i18n_domain='vindula_liberiuncontents',
            ),
            default='http://',
            required=True
    ), 
                                                                     
))

schemata.finalizeATCTSchema(SocialNetwork_schema, folderish=False)

invisible = {'view':'invisible','edit':'invisible',}
SocialNetwork_schema['description'].widget.visible = invisible

#Interface
class SocialNetwork(base.ATCTContent):
    """ Download Page """
    
    security = ClassSecurityInfo()
    implements(ISocialNetwork)    
    portal_type = 'SocialNetwork'
    _at_rename_after_creation = True
    schema = SocialNetwork_schema

registerType(SocialNetwork, PROJECTNAME) 