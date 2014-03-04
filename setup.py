import setuptools

# TODO: test_requires

setuptools.setup(
    zip_safe=True,
    name='cloudify-plugin-existing-server',
    version='0.1',
    author='Ilya Sher',
    author_email='ilya.sher@coding-knight.com',
    packages=['cloudify_plugin_existing_server'],
    license='LICENSE',
    description='Plugin for using existing servers',
)

