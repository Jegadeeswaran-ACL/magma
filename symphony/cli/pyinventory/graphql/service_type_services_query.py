#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin


@dataclass
class ServiceTypeServicesQuery(DataClassJsonMixin):
    @dataclass
    class ServiceTypeServicesQueryData(DataClassJsonMixin):
        @dataclass
        class Node(DataClassJsonMixin):
            @dataclass
            class Service(DataClassJsonMixin):
                @dataclass
                class Customer(DataClassJsonMixin):
                    id: str
                    name: str
                    externalId: Optional[str] = None

                id: str
                name: str
                externalId: Optional[str] = None
                customer: Optional[Customer] = None

            services: List[Service]

        serviceType: Optional[Node] = None

    data: ServiceTypeServicesQueryData

    __QUERY__: str = """
    query ServiceTypeServicesQuery($id: ID!) {
  serviceType: node(id: $id) {
    ... on ServiceType {
      services {
        id
        name
        externalId
        customer {
          id
          name
          externalId
        }
      }
    }
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, id: str) -> ServiceTypeServicesQueryData:
        # fmt: off
        variables = {"id": id}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data