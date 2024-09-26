from sklearn.model_selection import cross_val_predict
from sklearn.metrics import f1_score

def columns_to_drop_clf(model, X, y, f1):
    """
     drop each column one by one and see the effect on the model's performance, write a loop

     f1 - the threshold for the f1 score. If the f1 score is greater than this value, the column will be added to the list of columns to delete

     returns a list of columns to delete
    """
    to_delete = []
    for col in X.columns:
        
        X_copy = X.copy()
        X_copy = X_copy.drop(col, axis=1)
        y_train_pred = cross_val_predict(model, X_copy, y, cv=3)
        print(f'Column: {col}')
        print(f'F1 Score: {f1_score(y, y_train_pred)}')
        if f1_score(y, y_train_pred) > f1:
            to_delete.append(col)
    
    print(to_delete)