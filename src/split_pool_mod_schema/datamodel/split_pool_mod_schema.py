# Auto generated from split_pool_mod_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-28T08:16:06
# Schema: split-pool-mod-schema
#
# id: https://w3id.org/turbomam/split-pool-mod-schema
# description: A Schema with processes for splitting, pooling and modifying material entities. Intended to
#              illustrate solutions for NMDC modeling of NEON metadata and metabolomics data
# license: BSD-3

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPLIT_POOL_MOD_SCHEMA = CurieNamespace('split_pool_mod_schema', 'https://w3id.org/turbomam/split-pool-mod-schema/')
DEFAULT_ = SPLIT_POOL_MOD_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class MaterialEntityId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    An identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Database(YAMLRoot):
    """
    A possibly heterogeneous collections of data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Database
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Database

    named_thing_set: Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]] = empty_dict()
    material_entity_set: Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="named_thing_set", slot_type=NamedThing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="material_entity_set", slot_type=NamedThing, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    An entity that consists of matter
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.description, domain=None, range=Optional[str])

slots.named_thing_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.named_thing_set, name="named_thing_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('named_thing_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.named_thing_set, domain=None, range=Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]])

slots.material_entity_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, name="material_entity_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('material_entity_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, domain=None, range=Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]])