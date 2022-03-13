# The original form:
def generate_plot(data, image_name):
    """This function creates a scatter plot for the data"""
    # create the plot based on the data
    
    if image_name:
        # save the image
        
# In many cases, we don't need to save the image
generate_plot(data, None)



# The one with a default value
def generate_plot(data, image_name=None):
    pass
# Now, we can omit the second parameter
generate_plot(data)