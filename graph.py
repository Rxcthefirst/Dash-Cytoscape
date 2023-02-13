import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

container = html.Div(
    style={
        'width': '100%',
        'height': '100%',
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'justify-content': 'center'
    }
)

nodes = [
    {
        "data": {
            "id": "Mortgage Loan",
            "name": "Mortgage Loan",
            "definition": "A mortgage loan is ...",
            "semanticType": "Subject Area",
            "visibility": 1,
            "label": "Mortgage Loan",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Loan",
            "name": "Loan",
            "definition": "...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Loan",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Financial Instrument",
            "name": "Financial Instrument",
            "definition": "A Financial Instrument ...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Financial Instrument",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
{
        "data": {
            "id": "Adjustable Rate Mortgage",
            "name": "Adjustable Rate Mortgage",
            "definition": "A mortgage loan ...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Adjustable Rate Mortgage",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },{
        "data": {
            "id": "Fixed Rate Mortgage",
            "name": "Fixed Rate Mortgage",
            "definition": "A mortgage loan ...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Fixed Rate Mortgage",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Reverse Mortgage",
            "name": "Reverse Mortgage",
            "definition": "...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Reverse Mortgage",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Loan State",
            "name": "Loan State",
            "definition": "...",
            "semanticType": "Phase",
            "visibility": 2,
            "label": "Loan State",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Borrower",
            "name": "Borrower",
            "definition": "...",
            "semanticType": "Role",
            "visibility": 2,
            "label": "Borrower",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Real Property",
            "name": "Real Property",
            "definition": "...",
            "semanticType": "Role",
            "visibility": 2,
            "label": "Real Property",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Party Group",
            "name": "Party Group",
            "definition": "...",
            "semanticType": "Entity",
            "visibility": 2,
            "label": "Party Group",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "Loan Seller",
            "name": "Loan Seller",
            "definition": "...",
            "semanticType": "Role",
            "visibility": 2,
            "label": "Loan Seller",
            "color": "red",
            "size": 30,
            "custom_property": "value"
        }
    },
]

edges = [
    {
        "data": {
            "id": "edge1",
            "source": "Mortgage Loan",
            "target": "Financial Instrument",
            "label": "hasGeneral",
            "color": "blue",
            "width": 2,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "edge2",
            "source": "Mortgage Loan",
            "target": "Loan",
            "label": "referencedBySubjectArea",
            "color": "blue",
            "width": 2,
            "custom_property": "value"
        }
    },
    {
        "data": {
            "id": "edge3",
            "source": "Mortgage Loan",
            "target": "Adjustable Rate Mortgage",
            "label": "hasSpecific",
            "color": "blue",
            "width": 2,
            "custom_property": "value"
        }
    },
]

elements = edges + nodes

def mouseover_node_data(node):
    return {
        'id': node['data']['id'],
        'label': node['data']['label'],
        'definition': node['data']['definition']
    }

app.layout = html.Div(
    children=[
        container,
        cyto.Cytoscape(
            id='cytoscape-component',
            elements=elements,
            layout={'name': 'cose', 'edgeElasticity': 100},
            stylesheet=[
                {
                    'selector': 'node',
                    'style': {
                        'background-color': '#00008B',
                        'label': 'data(label)'
                    }
                },
                {
                    'selector': 'edge',
                    'style': {
                        'width': 2,
                        #'line-color': '#A6E22E',
                        'line-style': 'bezier',
                        'target-arrow-color': '#00008B',
                        'target-arrow-shape': 'triangle'
                    }
                },
                {
                    'selector': 'node[semanticType = "Entity"]',
                    'style': {
                        'background-color': 'red'
                    }
                },
                {
                    'selector': 'node[semanticType = "Role"]',
                    'style': {
                        'background-color': 'green'
                    }
                },
                {
                    'selector': 'node[semanticType = "Subject Area"]',
                    'style': {
                        'background-color': 'grey'
                    }
                },
                {
                    'selector': 'node[semanticType = "Phase"]',
                    'style': {
                        'background-color': 'purple'
                    }
                }
            ],
            style={
                'width': '100%',
                'height': '800px'
            }
        ),
        html.Div(id='hover-data', style={'margin-top': '20px'}),
        html.Div(id='hover-node-id', style={'display': 'none'})
    ]
)

@app.callback(
    dash.dependencies.Output('hover-data', 'children'),
    [dash.dependencies.Input('cytoscape-component', 'mouseoverNodeData')]
)

def display_hover_data(hover_data):
    if hover_data:
        return html.P(
            f'Node ID: {hover_data["id"]}\nNode Label: {hover_data["label"]}\nNode Definition: {hover_data["definition"]}',
            style={'font-size': '14px'})
    else:
        return html.P('No node data to display', style={'font-size': '14px'})

if __name__ == '__main__':
    app.run_server(debug=True)
