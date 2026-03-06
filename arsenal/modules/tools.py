#!/usr/bin/env python3

import shutil
import json
import os
from os.path import join

# Import config for file paths
from . import config


class ToolDetector:
    """Detects and caches tool availability and naming conventions"""

    def __init__(self):
        self.impacket_format = None  # Will be 'impacket', 'py', or None
        self.cache_file = getattr(
            config, "toolsfile", join(config.HOMEPATH, ".arsenal_tools.json")
        )
        self._load_cache()

    def _load_cache(self):
        """Load cached tool detection results"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r") as f:
                    cache = json.load(f)
                    self.impacket_format = cache.get("impacket_format")
            except (json.JSONDecodeError, IOError):
                # Corrupted cache, will re-detect
                pass

    def _save_cache(self):
        """Save tool detection results to cache"""
        try:
            with open(self.cache_file, "w") as f:
                json.dump({"impacket_format": self.impacket_format}, f)
        except IOError:
            # Can't write cache, not critical
            pass

    def detect_impacket_format(self):

        # Check for user override first
        if hasattr(config, 'IMPACKET_FORMAT_OVERRIDE') and config.IMPACKET_FORMAT_OVERRIDE:
            override = config.IMPACKET_FORMAT_OVERRIDE.lower()
            if override in ['impacket', 'py']:
                self.impacket_format = override
                return override
        
        if self.impacket_format is not None:

            return self.impacket_format

        # Common impacket tools to check
        tools_to_check = [
            "psexec",
            "smbexec",
            "wmiexec",
            "secretsdump",
            "GetNPUsers",
            "GetUserSPNs",
        ]

        # Check for pipx format FIRST (*.py)
        for tool in tools_to_check:
            if shutil.which(f"{tool}.py"):
                self.impacket_format = "py"
                self._save_cache()
                return "py"
        
        # Check for Kali format SECOND (impacket-*)
        for tool in tools_to_check:
            if shutil.which(f"impacket-{tool}"):
                self.impacket_format = "impacket"
                self._save_cache()
                return "impacket"

        self.impacket_format = None
        self._save_cache()
        return None

    def get_impacket_command(self, tool_name):
     
        fmt = self.detect_impacket_format()

        if fmt == "impacket":
            return f"impacket-{tool_name}"
        elif fmt == "py":
            return f"{tool_name}.py"
        else:

            return f"{tool_name}.py"


_detector = ToolDetector()


def detect_impacket_format():

    return _detector.detect_impacket_format()


def get_impacket_command(tool_name):

    return _detector.get_impacket_command(tool_name)
