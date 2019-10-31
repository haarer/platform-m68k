# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Default flags for bare-metal programming (without any framework layers)
#

from SCons.Script import Import

Import("env")

env.Append(

    ASFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=[
    ],

    CCFLAGS=[
        "-O2",  # optimize for speed
        "-Wall",  # show warnings
        "-DREENTRANT_SYSCALLS_PROVIDED",
        "-D_REENT_SMALL",
        "-m$BOARD_MCU",
        "-std=gnu99",
        "-g"
    ],

    CXXFLAGS=[
        "-Wno-error=narrowing",
        "-fno-exceptions",
        "-fno-threadsafe-statics",
        "-fpermissive",
        "-std=gnu++11"
    ],

    CPPDEFINES=[
        ("F_CPU", "$BOARD_F_CPU")
    ],

    LINKFLAGS=[
        "-m$BOARD_MCU",
        "-g",
 #       "-Wl,--script=bcc.ld,-Map=m68k-test.map,--allow-multiple-definition",
        "--verbose"
    ],


    LIBS=[]
)

# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])
