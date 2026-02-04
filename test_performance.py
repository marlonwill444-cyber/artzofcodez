#!/usr/bin/env python3
"""
Simple performance test to verify optimizations.
This tests that the code runs without errors and validates the improvements.
"""

import sys
import time
from unittest.mock import Mock, patch, MagicMock

# Import the modules to test
import mdigitalartz_leonardo
import generate_aether_core


def test_headers_caching():
    """Test that headers are cached and not recreated on every call."""
    print("Testing header caching...")
    
    # Check that _HEADERS exists and is a dict
    assert hasattr(mdigitalartz_leonardo, '_HEADERS'), "Missing _HEADERS constant"
    assert isinstance(mdigitalartz_leonardo._HEADERS, dict), "_HEADERS should be a dict"
    assert 'Authorization' in mdigitalartz_leonardo._HEADERS, "Missing Authorization header"
    assert 'Content-Type' in mdigitalartz_leonardo._HEADERS, "Missing Content-Type header"
    
    # Same for generate_aether_core
    assert hasattr(generate_aether_core, '_HEADERS'), "Missing _HEADERS in generate_aether_core"
    assert isinstance(generate_aether_core._HEADERS, dict), "_HEADERS should be a dict"
    
    print("✓ Headers are cached as constants")


def test_session_reuse():
    """Test that session is created once and reused."""
    print("\nTesting session reuse...")
    
    # Get session multiple times and verify it's the same instance
    session1 = mdigitalartz_leonardo._get_session()
    session2 = mdigitalartz_leonardo._get_session()
    
    assert session1 is session2, "Session should be reused, not recreated"
    print("✓ Session is reused across calls")


def test_timeout_configuration():
    """Test that timeouts are configured."""
    print("\nTesting timeout configuration...")
    
    assert hasattr(mdigitalartz_leonardo, 'REQUEST_TIMEOUT'), "Missing REQUEST_TIMEOUT"
    assert mdigitalartz_leonardo.REQUEST_TIMEOUT == (10, 30), "Incorrect timeout values"
    
    assert hasattr(generate_aether_core, 'REQUEST_TIMEOUT'), "Missing REQUEST_TIMEOUT in generate_aether_core"
    
    print("✓ Timeouts are configured")


def test_environment_variable_support():
    """Test that API key can be read from environment variable."""
    print("\nTesting environment variable support...")
    
    # Test with mock environment variable
    with patch.dict('os.environ', {'LEONARDO_API_KEY': 'test-key-from-env'}):
        # Reload the module to pick up the environment variable
        import importlib
        importlib.reload(mdigitalartz_leonardo)
        
        # The API_KEY should now be from the environment
        assert mdigitalartz_leonardo.API_KEY == 'test-key-from-env', "Should read API key from environment"
    
    # Reload again to restore original
    import importlib
    importlib.reload(mdigitalartz_leonardo)
    
    print("✓ Environment variable support works")


def test_json_parameter_usage():
    """Test that functions use json parameter instead of data=json.dumps()."""
    print("\nTesting json parameter usage...")
    
    # Mock the requests to verify the parameters
    mock_response = Mock()
    mock_response.json.return_value = {"generationId": "test-id"}
    mock_response.raise_for_status = Mock()
    
    mock_session = Mock()
    mock_session.post.return_value = mock_response
    
    with patch.object(mdigitalartz_leonardo, '_get_session', return_value=mock_session):
        # Call the function
        result = mdigitalartz_leonardo.generate_images_phoenix("test prompt")
        
        # Verify that post was called with json parameter, not data
        assert mock_session.post.called, "Session.post should be called"
        call_kwargs = mock_session.post.call_args[1]
        assert 'json' in call_kwargs, "Should use json parameter"
        assert 'data' not in call_kwargs, "Should not use data parameter"
        assert 'timeout' in call_kwargs, "Should include timeout"
    
    print("✓ Functions use json parameter correctly")


def test_no_old_functions():
    """Test that old inefficient functions are removed."""
    print("\nTesting removal of old functions...")
    
    # _make_headers should not exist anymore
    assert not hasattr(mdigitalartz_leonardo, '_make_headers'), \
        "_make_headers should be removed (replaced with _HEADERS constant)"
    
    assert not hasattr(generate_aether_core, '_make_headers'), \
        "_make_headers should be removed from generate_aether_core"
    
    print("✓ Old inefficient functions removed")


def run_all_tests():
    """Run all performance tests."""
    print("=" * 60)
    print("Running Performance Optimization Tests")
    print("=" * 60)
    
    try:
        test_headers_caching()
        test_session_reuse()
        test_timeout_configuration()
        test_environment_variable_support()
        test_json_parameter_usage()
        test_no_old_functions()
        
        print("\n" + "=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
