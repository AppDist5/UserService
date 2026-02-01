from flask import jsonify

def error_handler(error):
    print(f'Error: {error}')
    
    status = getattr(error, 'status', 500)
    code = getattr(error, 'code', 'INTERNAL_ERROR')
    message = str(error) or 'Error interno del servidor'
    
    return jsonify({
        'error': True,
        'message': message,
        'code': code
    }), status