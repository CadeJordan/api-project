
from pytest import raises
from tft.main import TftAppTest

def test_tft():
    # test tft without any subcommands or arguments
    with TftAppTest() as app:
        app.run()
        assert app.exit_code == 0


def test_tft_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with TftAppTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with TftAppTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with TftAppTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')
