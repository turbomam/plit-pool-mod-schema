# Auto generated from split_pool_mod_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-28T13:27:31
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
BIOPROJECT = CurieNamespace('BIOPROJECT', 'https://www.ncbi.nlm.nih.gov/bioproject/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NEON_SAMP_VIEW = CurieNamespace('NEON_SAMP_VIEW', 'https://data.neonscience.org/api/v0/samples/view?')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPLIT_POOL_MOD_SCHEMA = CurieNamespace('split_pool_mod_schema', 'https://w3id.org/turbomam/split-pool-mod-schema/')
DEFAULT_ = SPLIT_POOL_MOD_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class DatabaseId(URIorCURIE):
    pass


class MaterialEntityId(NamedThingId):
    pass


class ProcessId(NamedThingId):
    pass


class InformationId(NamedThingId):
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

    id: Union[str, DatabaseId] = None
    name: Optional[str] = None
    information_set: Optional[Union[Dict[Union[str, InformationId], Union[dict, "Information"]], List[Union[dict, "Information"]]]] = empty_dict()
    material_entity_set: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()
    named_thing_set: Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]] = empty_dict()
    process_set: Optional[Union[Dict[Union[str, ProcessId], Union[dict, "Process"]], List[Union[dict, "Process"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseId):
            self.id = DatabaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="information_set", slot_type=Information, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="material_entity_set", slot_type=MaterialEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="named_thing_set", slot_type=NamedThing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="process_set", slot_type=Process, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    An entity that consists of matter. Has an identity that persists over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MaterialEntity
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Process(NamedThing):
    """
    An entity that unfolds over time. Not composed of matter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Process
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Process

    id: Union[str, ProcessId] = None
    has_inputs: Optional[Union[str, List[str]]] = empty_list()
    has_outputs: Optional[Union[str, List[str]]] = empty_list()
    has_input: Optional[Union[str, NamedThingId]] = None
    has_output: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, str) else str(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, str) else str(v) for v in self.has_outputs]

        if self.has_input is not None and not isinstance(self.has_input, NamedThingId):
            self.has_input = NamedThingId(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, NamedThingId):
            self.has_output = NamedThingId(self.has_output)

        super().__post_init__(**kwargs)


@dataclass
class Information(NamedThing):
    """
    Anything that informs, or reduces uncertainty. Can be about a material entity or a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Information
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Information"
    class_name: ClassVar[str] = "Information"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Information

    id: Union[str, InformationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationId):
            self.id = InformationId(self.id)

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
                   model_uri=SPLIT_POOL_MOD_SCHEMA.named_thing_set, domain=Database, range=Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]])

slots.material_entity_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, name="material_entity_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('material_entity_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, domain=Database, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]])

slots.process_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.process_set, name="process_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('process_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.process_set, domain=Database, range=Optional[Union[Dict[Union[str, ProcessId], Union[dict, "Process"]], List[Union[dict, "Process"]]]])

slots.information_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.information_set, name="information_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('information_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.information_set, domain=Database, range=Optional[Union[Dict[Union[str, InformationId], Union[dict, "Information"]], List[Union[dict, "Information"]]]])

slots.has_inputs = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_inputs, name="has_inputs", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_inputs'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_inputs, domain=Process, range=Optional[Union[str, List[str]]])

slots.has_outputs = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_outputs, name="has_outputs", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_outputs'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_outputs, domain=Process, range=Optional[Union[str, List[str]]])

slots.has_input = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_input, name="has_input", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_input'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_input, domain=Process, range=Optional[Union[str, NamedThingId]])

slots.has_output = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_output, name="has_output", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_output'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_output, domain=Process, range=Optional[Union[str, NamedThingId]])