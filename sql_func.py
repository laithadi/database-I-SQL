"""
-------------------------------------------------------
functions.py
Fall 2020
-------------------------------------------------------
Author:  Laith Adi 
ID:      170265190
Email:   adix5190@wlu.ca
-------------------------------------------------------
"""
# -----------------------------------------------------------------------------
# task 1
# -----------------------------------------------------------------------------
def table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = table_info(cursor, table_schema)
    Use: rows = table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, TABLE_TYPE
        (list of ?)
    -------------------------------------------------------
    """
    
    parameter = None 

    if table_name is None: 
        sql = """SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
        FROM information_schema.TABLES
        WHERE table_schema = %s
        ORDER BY TABLE_NAME, TABLE_TYPE"""

        parameter = [table_schema]

    else: 
        sql = """ SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
        FROM information_schema.TABLES
        WHERE table_schema = %s AND table_name = %s 
        ORDER BY TABLE_NAME, TABLE_TYPE """
        
        parameter = [table_schema,table_name]

    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows
    

# -----------------------------------------------------------------------------
# task 2
# -----------------------------------------------------------------------------
def column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = column_info(cursor, table_schema)
    Use: rows = column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None 

    if table_name is None: 
        sql = """SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
        FROM information_schema.COLUMNS
        WHERE table_schema = %s
        ORDER BY TABLE_NAME, COLUMN_NAME"""
        
        parameter = [table_schema]
        
    else: 
        sql = """SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
        FROM information_schema.COLUMNS
        WHERE table_schema = %s AND table_name = %s 
        ORDER BY TABLE_NAME, COLUMN_NAME"""
        
        parameter = [table_schema,table_name]

    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows


# -----------------------------------------------------------------------------
# task 3
# -----------------------------------------------------------------------------
def constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = constraint_info(cursor, table_schema)
    Use: rows = constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields.
        If constraint_type is None
            returns data for all constraints
        Otherwise
            returns data for constraint whose type matches constraint_type
        Sorted by CONSTRAINT_NAME, TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None 

    if constraint_type is None: 
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE table_schema = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME"""
        
        parameter = [table_schema]

    else: 
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE table_schema = %s AND constraint_type = %s 
        ORDER BY CONSTRAINT_NAME, TABLE_NAME"""
    
        parameter = [table_schema,constraint_type]
    
    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows
    

# -----------------------------------------------------------------------------
# task 4
# -----------------------------------------------------------------------------
def foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = foreign_key_info(cursor, constraint_schema)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None

    if table_name is None and ref_table_name is None: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema]
    
    elif table_name is None and ref_table_name is not None: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND ref_table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,ref_table_name]
    
    elif ref_table_name is None and table_name is not None:
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,table_name]
   
    else: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND table_name = %s AND ref_table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,table_name,ref_table_name]

    cursor.execute(sql,parameter)    
    rows = cursor.fetchall()
    return rows 


# -----------------------------------------------------------------------------
# task 5
# -----------------------------------------------------------------------------
def key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = key_info(cursor, constraint_schema)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    pass
    
    
    
    ---------------------------------------------------------------------------------------------------------
    """
-------------------------------------------------------
functions.py
Fall 2020
-------------------------------------------------------
Author:  Laith Adi 
ID:      170265190
Email:   adix5190@wlu.ca
-------------------------------------------------------
"""
# -----------------------------------------------------------------------------
# task 1
# -----------------------------------------------------------------------------
def pub_counts_all(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the numbers of publications of each type. Name these
            three fields "articles", "papers", and "books".
        If member_id is None
            returns numbers of publications for all members
        Otherwise
            returns numbers of publications for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """ 
    parameter = None
    
    if member_id is None:
        sql = """
            SELECT m.last_name, m.first_name,
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_id AND pub_type_id = 'a') AS articles,     
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_id AND pub_type_id = 'p') AS papers,    
            (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_id AND pub_type_id = 'b') AS books       
            FROM member AS m
            ORDER BY m.last_name, m.first_name
        """

    else:
        sql = """
            SELECT m.last_name, m.first_name, 
            (SELECT COUNT(*) FROM pub AS p WHERE p.member_id = %s AND p.pub_type_id = 'a') AS articles,
            (SELECT COUNT(*) FROM pub AS p WHERE %s = p.member_id AND pub_type_id = 'p') AS papers,    
            (SELECT COUNT(*) FROM pub AS p WHERE %s = p.member_id AND pub_type_id = 'b') AS books       
            FROM member AS m,
            WHERE m.member_id = %s,
            ORDER BY m.last_name, m.first_name
        """

        parameter = [member_id, member_id, member_id, member_id]
    
    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    
    return rows


# -----------------------------------------------------------------------------
# task 2
# -----------------------------------------------------------------------------
def expertise_count(cursor, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(cursor)
    Use: rows = expertise_count(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the number of keywords and supplementary keywords
            for the member. Name these fields "keywords" and "supp_keys".
        If member_id is None
            returns numbers of expertises for all members
        Otherwise
            returns numbers of expertises for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """
    parameter = None 

    if member_id is None:
        sql = """
            SELECT m.last_name, m.first_name, 
            (SELECT COUNT(*) FROM member_keyword AS mk WHERE m.member_id = mk.member_id) AS keywords,
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE m.member_id = msk.member_id) AS supp_keys
            FROM member AS m,
            ORDER BY m.last_name, m.first_name
        """

    else:
        sql = """
            SELECT m.last_name, m.first_name, 
            (SELECT COUNT(*) FROM member_keyword AS mk WHERE %s = mk.member_id) AS keywords,
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE %s = msk.member_id) AS supp_keys
            FROM member AS m,
            WHERE m.member_id = %s, 
            ORDER BY m.last_name, m.first_name
        """

        parameter = [member_id, member_id, member_id]

    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    
    return rows



# -----------------------------------------------------------------------------
# task 3
# -----------------------------------------------------------------------------
def keyword_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(cursor)
    Use: rows = keyword_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
            supplementary keywords that belong to it. Name the second field
            "supp_key_count".
        If keyword_id is None
            returns numbers of supplementary keywords for all keywords
        Otherwise
            returns numbers of supplementary keywords for the keyword matching
                keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    parameter = None 

    if keyword_id is None:
        sql = """
            SELECT k.k_desc,
            (SELECT COUNT(*) FROM supp_key AS sk WHERE k.keyword_id = sk.keyword_id) AS supp_key_count
            FROM keyword AS k,
            ORDER BY k.k_desc 
        """
    
    else:
        sql = """
            SELECT k.k_desc, 
            (SELECT COUNT(*) FROM supp_key AS sk WHERE %s = sk.keyword_id) AS supp_key_count
            FROM keyword AS k,
            WHERE k.keyword = %s,
            ORDER BY k.k_desc
        """

        parameter = [keyword_id, keyword_id]  

    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    
    return rows


# -----------------------------------------------------------------------------
# task 4
# -----------------------------------------------------------------------------
def keyword_member_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(cursor)
    Use: rows = keyword_member_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword description and the number of members
            that have it. Name the second field "member_count".
        If keyword_id is None
            returns numbers of members for all keywords
        Otherwise
            returns numbers of members for the keyword matching keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    parameter = None 

    if keyword_id is None:
        sql = """
            SELECT k.k_desc,
            (SELECT COUNT(*) FROM member_keyword AS mk WHERE k.keyword = mk.keyword) AS member_count
            FROM keyword AS k,
            ORDER k.desc
        """

    else:
        sql = """
            SELECT k.k_desc,
            (SELECT COUNT(mk.member_id) FROM member_keyword AS mk WHERE %s = mk.keyword) AS member_count
            FROM keyword AS k,
            WHERE k.keyword_id = %s,
            ORDER k.desc
        """

        parameter = [keyword_id, keyword_id]

    cursor.execute(sql, parameter)
    rows = cursor.fetchall()

    return rows 





# -----------------------------------------------------------------------------
# task 5
# -----------------------------------------------------------------------------

def supp_key_member_count(cursor, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(cursor)
    Use: rows = supp_key_member_count(cursor, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
            keyword description, and the number of members that have that
            supplementary expertise. Name the last field "member_count".
        If supp_key_id is None
            returns numbers of members for all supplementary keywords
        Otherwise
            returns numbers of members for the supplementary keyword
            matching supp_key_id
        Sorted by keyword description and then supplementary keyword description
        (list of ?)
    -------------------------------------------------------
    """
    parameter = None 

    if supp_key_id is None:
        sql = """
            SELECT k.k_desc, sk.sk_desc, 
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE msk.supp_key_id = sk.supp_key_id) AS member_count
            FROM keyword AS k, supp_key AS sk 
            ORDER k.k_desc, sk.desc 
        """

    else:
        sql = """
            SELECT k.k_desc, sk.sk_desc, 
            (SELECT COUNT(*) FROM member_supp_key AS msk WHERE msk.supp_key_id = %s) AS member_count
            FROM keyword AS k, supp_key AS sk 
            WHERE sk = %s
            ORDER k.k_desc, sk.desc
        """

        parameter = [supp_key_id, supp_key_id] 

    cursor.execute(sql, parameter)
    rows = cursor.fetchall()

    return rows 

---------------------------------------------------------------------------------------------------------

"""
-------------------------------------------------------
functions.py
Fall 2020
-------------------------------------------------------
Author:  Laith Adi 
ID:      170265190
Email:   adix5190@wlu.ca
-------------------------------------------------------
"""
# -----------------------------------------------------------------------------
# task 1
# -----------------------------------------------------------------------------
def table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = table_info(cursor, table_schema)
    Use: rows = table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, TABLE_TYPE
        (list of ?)
    -------------------------------------------------------
    """
    
    parameter = None 

    if table_name is None: 
        sql = """SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
        FROM information_schema.TABLES
        WHERE table_schema = %s
        ORDER BY TABLE_NAME, TABLE_TYPE"""

        parameter = [table_schema]

    else: 
        sql = """ SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
        FROM information_schema.TABLES
        WHERE table_schema = %s AND table_name = %s 
        ORDER BY TABLE_NAME, TABLE_TYPE """
        
        parameter = [table_schema,table_name]

    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows
    

# -----------------------------------------------------------------------------
# task 2
# -----------------------------------------------------------------------------
def column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = column_info(cursor, table_schema)
    Use: rows = column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None 

    if table_name is None: 
        sql = """SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
        FROM information_schema.COLUMNS
        WHERE table_schema = %s
        ORDER BY TABLE_NAME, COLUMN_NAME"""
        
        parameter = [table_schema]
        
    else: 
        sql = """SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
        FROM information_schema.COLUMNS
        WHERE table_schema = %s AND table_name = %s 
        ORDER BY TABLE_NAME, COLUMN_NAME"""
        
        parameter = [table_schema,table_name]

    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows


# -----------------------------------------------------------------------------
# task 3
# -----------------------------------------------------------------------------
def constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = constraint_info(cursor, table_schema)
    Use: rows = constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields.
        If constraint_type is None
            returns data for all constraints
        Otherwise
            returns data for constraint whose type matches constraint_type
        Sorted by CONSTRAINT_NAME, TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None 

    if constraint_type is None: 
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE table_schema = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME"""
        
        parameter = [table_schema]

    else: 
        sql = """SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE table_schema = %s AND constraint_type = %s 
        ORDER BY CONSTRAINT_NAME, TABLE_NAME"""
    
        parameter = [table_schema,constraint_type]
    
    cursor.execute(sql,parameter)
    rows = cursor.fetchall()
    return rows
    

# -----------------------------------------------------------------------------
# task 4
# -----------------------------------------------------------------------------
def foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = foreign_key_info(cursor, constraint_schema)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """

    parameter = None

    if table_name is None and ref_table_name is None: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema]
    
    elif table_name is None and ref_table_name is not None: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND ref_table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,ref_table_name]
    
    elif ref_table_name is None and table_name is not None:
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,table_name]
   
    else: 
        sql = """SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE constraint_schema = %s AND table_name = %s AND ref_table_name = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME """
        
        parameter = [constraint_schema,table_name,ref_table_name]

    cursor.execute(sql,parameter)    
    rows = cursor.fetchall()
    return rows 


# -----------------------------------------------------------------------------
# task 5
# -----------------------------------------------------------------------------
def key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = key_info(cursor, constraint_schema)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    pass






