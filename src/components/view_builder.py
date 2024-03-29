def view_builder(json_data, update):
    table_data = ""

    # Changing view as per the update status.
    if update == True:
        for row in json_data:
            table_heading = """
                        <tr>
                            <th> Name </th>
                            <th> Repo </th>
                            <th> Version </th>
                            <th> Version_Satisfied </th>
                            <th> PR Link </th>
                        </tr>
                            """
            table_data = (
                table_data
                + f"""
                            <tr>
                                <td> {json_data[row][0]} </td>
                                <td> {json_data[row][1]} </td>
                                <td> {json_data[row][2]} </td>
                                <td> {json_data[row][3]} </td>
                                <td> <a href={json_data[row][4]}> {json_data[row][4]} </a> </td>
                            </tr>"""
            )
    else:
        table_heading = """
                        <tr>
                            <th> Name </th>
                            <th> Repo </th>
                            <th> Version </th>
                            <th> Version_Satisfied </th>
                        </tr>
                            """
        for row in json_data:
            table_data = (
                table_data
                + f"""
                            <tr>
                                <td> {json_data[row][0]} </td>
                                <td> {json_data[row][1]} </td>
                                <td> {json_data[row][2]} </td>
                                <td> {json_data[row][3]} </td>
                            </tr>"""
            )

    # Final HTML Table rendering.
    view = f"""
        <html>
            <head>
                <title> Result from Query </title>
                <style>
                table, th, td \u007b
                        border: 1px solid black;
                        padding: 15px;
                        \u007d
                    tr:hover \u007bbackground-color: #D6EEEE;\u007d
                </style>
            </head>
            <body>
                <h2> Result from Query </h2>
                <table style="width:100%">
                    <thead>
                        {table_heading}
                    </thead>
                    <tbody>
                        {table_data}
                    </tbody>
                </table>
            </body>
        """
    return view
