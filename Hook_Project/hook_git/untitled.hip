HouNC1033600baa063da135d09a7e5953.start fplayback -i on -r off -f 1 -e on -h on -t on -a on -k on -s 1
tcur 0
fps 24
tset 0 10
frange 1 240
unitlength 1
unitmass 1
prompt '`strcat(oppwf(), " -> ")`'
HouNC1033600ba6063da135d043eeba7e.variables set -g ACTIVETAKE = 'Main'
set -g E = '2.7182818284590452354'
set -g EYE = 'stereo'
set -g HIP = '/home/rapa/PycharmProject/HookProject'
set -g HIPFILE = '/home/rapa/PycharmProject/HookProject/untitled.hip'
set -g HIPNAME = 'untitled'
set -g JOB = '/home/rapa/PycharmProject/HookProject'
set -g PI = '3.1415926535897932384'
set -g POSE = '/home/rapa/houdini19.5/poselib'
set -g _HIP_SAVEPLATFORM = 'linux-x86_64-gcc9.3'
set -g _HIP_SAVETIME = 'Wed Feb  1 16:23:09 2023'
set -g _HIP_SAVEVERSION = '19.5.493'
set -g status = '0'
HouNC1033600ba4063da135d0dba5575b.aliases alias bye 'quit'
alias cd 'opcf'
alias cp 'opcp'
alias h 'history'
alias hython 'python'
alias ls 'opls'
alias matramp 'opramp'
alias opcd 'opcf'
alias oppwd 'oppwf'
alias pwd 'oppwf'
alias rm 'oprm'
HouNC1033600ba1063da135d04309e1eb.takeconfig takename -g take
HouNC1033600ba0063da135d0e36d4a3d.hou.session HouNC1033600ba0063da135d08029b1f6.OPlibraries HouNC1033600ba2063da135d06c0e60b2.OPpreferences HouNC1033600ba0063da135d0757665dd.OPfallbacks Top/localscheduler /opt/hfs19.5.493/houdini/otls/OPlibTop.hda
Top/localscheduler otls/OPlibTop.hda
HouNC1033600ba0063da135d08cfae4ab.OPdummydefs INDX              INDEX_SECTION       ?c?]   houdini.hdalibrary   ?    c?]   Top/localscheduler   ?  ??c?]         localscheduler   Local Scheduler   ,oplib:/Top/localscheduler?Top/localscheduler   TOP_localscheduler           Top               <pdgtype='scheduler' subtype=localscheduler visibleoutputs=0         c?]      INDX              DialogScript      ?Vc??# Dialog script for localscheduler automatically generated

{
    name	localscheduler
    script	localscheduler
    label	"Local Scheduler"

    help {
	""
    }

    group {
        name    "folder0"
        label   "Scheduler"

        groupsimple {
            name    "folder5"
            label   "Scheduling"

            parm {
                name    "maxprocsmenu"
                label   "Total Slots"
                type    ordinal
                joinnext
                default { "0" }
                menu usetokenvalue {
                    "0"     "Equal to 1/4 of Total CPU Count"
                    "-1"    "Equal to CPU Count Less One"
                    "1"     "Custom Slot Count"
                }
            }
            parm {
                name    "maxprocs"
                label   "maxprocs"
                type    integer
                nolabel
                default { "1" }
                disablewhen "{ maxprocsmenu != 1 }"
                range   { -4 128 }
                parmtag { "autoscope" "0000000000000000" }
            }
            parm {
                name    "verbose"
                label   "Verbose Logging"
                type    toggle
                default { "0" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_waitforfailures"
                label   "Block on Failed Work Items"
                type    toggle
                default { "0" }
                parmtag { "script_callback_language" "python" }
            }
        }

        groupsimple {
            name    "folder4"
            label   "Paths"

            parm {
                name    "pdg_workingdir"
                label   "Working Directory"
                type    directory
                default { "$HIP" }
            }
            parm {
                name    "pdg_workitemdatasource"
                label   "Load Item Data From"
                type    ordinal
                default { "0" }
                menu {
                    "0" "Temporary JSON File"
                    "1" "RPC Message"
                }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_compressworkitemdata"
                label   "Compress Work Item Data"
                type    toggle
                default { "1" }
                disablewhen "{ pdg_workitemdatasource == 1 }"
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_validateoutputs"
                label   "Validate Outputs When Recooking"
                type    toggle
                default { "1" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_checkexpectedoutputs"
                label   "Check Expected Outputs on Disk"
                type    toggle
                default { "1" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "sepparm2"
                label   "Separator"
                type    separator
                default { "" }
            }
            parm {
                name    "pdg_mapmode"
                label   "Path Mapping"
                type    ordinal
                default { "0" }
                menu {
                    "0" "Global"
                    "1" "None"
                }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_usemapzone"
                label   "Use Path Map Zone"
                type    toggle
                nolabel
                joinnext
                default { "0" }
                disablewhen "{ pdg_mapmode == 1 }"
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "pdg_mapzone"
                label   "Path Map Zone"
                type    string
                default { "$PDG_PATHMAP_ZONE" }
                disablewhen "{ pdg_usemapzone == 0 }"
                menureplace {
                    "POSIX" "POSIX"
                    "WIN"   "WIN"
                }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "sepparm3"
                label   "Separator"
                type    separator
                default { "" }
            }
            groupsimple {
                name    "folder1"
                label   "Temp Directory"

                parm {
                    name    "tempdirmenu"
                    label   "Location"
                    type    ordinal
                    default { "1" }
                    menu {
                        "0" "Working Directory"
                        "1" "Houdini Temp"
                        "2" "Custom"
                    }
                }
                parm {
                    name    "tempdirappendpid"
                    label   "Append PID"
                    type    toggle
                    default { "1" }
                }
                parm {
                    name    "tempdircustom"
                    label   "Custom"
                    type    directory
                    default { "$HOUDINI_TEMP_DIR/$HIPNAME/pdgtemp" }
                    disablewhen "{ tempdirmenu != 2 }"
                }
            }

        }

        parm {
            name    "socketcallbacks"
            label   "Use Socket callbacks instead of stdout tokens"
            type    integer
            invisible
            default { "1" }
            range   { 0 10 }
        }
    }

    group {
        name    "folder0_1"
        label   "RPC Server"

        parm {
            name    "pdg_rpcignoreerrors"
            label   "Ignore RPC Errors"
            type    ordinal
            default { "0" }
            menu {
                "0" "Never"
                "1" "When Cooking Batches"
                "2" "Always"
            }
            parmtag { "script_callback_language" "python" }
        }
        parm {
            name    "pdg_rpctimeout"
            label   "Connection Timeout"
            type    integer
            default { "4" }
            range   { 0 10 }
            parmtag { "script_callback_language" "python" }
        }
        parm {
            name    "pdg_rpcretries"
            label   "Connection Retries"
            type    integer
            default { "2" }
            range   { 0 10 }
            parmtag { "script_callback_language" "python" }
        }
        parm {
            name    "pdg_rpcbackoff"
            label   "Retry Backoff"
            type    integer
            default { "2" }
            range   { 0 10 }
            parmtag { "script_callback_language" "python" }
        }
        parm {
            name    "pdg_rpcbatch"
            label   "Batch Poll Rate"
            type    float
            default { "1" }
            range   { 0 10 }
            parmtag { "script_callback_language" "python" }
        }
        parm {
            name    "pdg_rpcrelease"
            label   "Release Job Slot When Polling"
            type    toggle
            default { "1" }
            parmtag { "script_callback_language" "python" }
        }
    }

    group {
        name    "folder0_3"
        label   "Job Parms"

        groupsimple {
            name    "folder0_2"
            label   "Scheduling"

            parm {
                name    "local_single"
                label   "Single"
                type    toggle
                default { "0" }
                range   { 0 10 }
                parmtag { "pdg::scheduler" "" }
            }
            parm {
                name    "local_is_CPU_number_set"
                label   "local_is_CPU_number_set"
                type    toggle
                nolabel
                joinnext
                default { "0" }
                range   { 0 1 }
                parmtag { "pdg::scheduler" "" }
            }
            parm {
                name    "local_CPUs_to_use"
                label   "Slots Per Work Item"
                type    integer
                default { "1" }
                disablewhen "{ local_is_CPU_number_set == 0 }"
                range   { 1! 64 }
                parmtag { "pdg::scheduler" "" }
            }
            groupsimple {
                name    "folder6"
                label   "Minimum Available Memory"

                parm {
                    name    "local_useminfreemem"
                    label   "Rule"
                    type    ordinal
                    default { "0" }
                    menu {
                        "0" "No Minimum"
                        "1" "MB Available"
                        "2" "Percent Available"
                    }
                    parmtag { "pdg::scheduler" "" }
                    parmtag { "script_callback_language" "python" }
                }
                parm {
                    name    "local_minfreemem"
                    label   "Minimum MB"
                    type    float
                    default { "0" }
                    disablewhen "{ local_useminfreemem != 1 }"
                    range   { 0 128000 }
                    parmtag { "pdg::scheduler" "" }
                    parmtag { "script_callback_language" "python" }
                }
                parm {
                    name    "local_minfreemempct"
                    label   "Minimum Percent"
                    type    float
                    default { "0" }
                    disablewhen "{ local_useminfreemem != 2 }"
                    range   { 0 1 }
                    parmtag { "pdg::scheduler" "" }
                    parmtag { "script_callback_language" "python" }
                }
            }

        }

        groupsimple {
            name    "folder2"
            label   "Tasks"

            parm {
                name    "local_enabletimeout"
                label   "Enable Maximum Run Time"
                type    toggle
                nolabel
                joinnext
                default { "0" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_maxtime"
                label   "Maximum Run Time"
                type    float
                default { "0" }
                disablewhen "{ local_enabletimeout == 0 }"
                range   { 0 10 }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_handletimeout"
                label   "On Task Timeout"
                type    ordinal
                default { "0" }
                disablewhen "{ local_enabletimeout == 0 }"
                menu {
                    "0" "Mark as Failed"
                    "1" "Mark as Succeeded"
                }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "sepparm4"
                label   "Separator"
                type    separator
                default { "" }
            }
            parm {
                name    "local_echandleby"
                label   "On Task Failure"
                type    ordinal
                default { "0" }
                menu {
                    "0" "Report Error"
                    "1" "Report Warning"
                    "2" "Retry Task"
                    "3" "Ignore"
                }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_echandleall"
                label   "Handle All Non Zero"
                type    toggle
                default { "1" }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_eccustomcode"
                label   "Exit Code"
                type    integer
                default { "1" }
                disablewhen "{ local_echandleall != 0 }"
                range   { 1 255 }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "sepparm"
                label   "Separator"
                type    separator
                default { "" }
            }
            parm {
                name    "local_maximumretries"
                label   "Max Retries"
                type    integer
                default { "3" }
                disablewhen "{ local_echandleby != 2 }"
                range   { 0 10 }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_addfailcountattr"
                label   "Retry Count Attribute"
                type    toggle
                nolabel
                joinnext
                default { "0" }
                disablewhen "{ local_echandleby != 2 }"
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_failcountattr"
                label   "Retry Count Attrib"
                type    string
                default { "failurecount" }
                disablewhen "{ local_addfailcountattr == 0 } { local_echandleby != 2 }"
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
        }

        groupsimple {
            name    "folder3"
            label   "Task Environment"

            parm {
                name    "local_usehoudinimaxthreads"
                label   "local_usehoudinimaxthreads"
                type    toggle
                nolabel
                joinnext
                default { "0" }
                parmtag { "pdg::scheduler" "" }
            }
            parm {
                name    "local_houdinimaxthreads"
                label   "Houdini Max Threads"
                type    integer
                default { "0" }
                disablewhen "{ local_usehoudinimaxthreads == 0 }"
                range   { 0 10 }
                parmtag { "pdg::scheduler" "" }
            }
            parm {
                name    "local_requireswindow"
                label   "Requires GUI Window"
                type    toggle
                default { "0" }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_skippackages"
                label   "Skip Loading Packages"
                type    toggle
                default { "1" }
                parmtag { "script_callback_language" "python" }
            }
            parm {
                name    "local_envunset"
                label   "Unset Variables"
                type    string
                default { "" }
                parmtag { "pdg::scheduler" "" }
                parmtag { "script_callback_language" "python" }
            }
            multiparm {
                name    "local_envmulti"
                label    "Environment Variables"
                parmtag { "pdg::nocopy" "" }
                parmtag { "script_callback" "" }
                parmtag { "script_callback_language" "hscript" }

                parm {
                    name    "local_envname#"
                    label   "Name"
                    type    string
                    joinnext
                    default { "" }
                    parmtag { "pdg::scheduler" "" }
                }
                parm {
                    name    "local_envvalue#"
                    label   "Value"
                    type    string
                    default { "" }
                    parmtag { "pdg::scheduler" "" }
                }
            }

        }

    }

}
HouNC1033600bbd063da135d093af9ae7expression.func # 0 bytes
HouNC1033600ba5063da135d006d0ac5bvex.def comment ""
position 0 6
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed off
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236191
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba4063da135d05af56f87vex.parm {
version 0.8
}
HouNC1033600ba0063da135d084719914vex.userdata     ___Version___    19.5.493HouNC1033600ba5063da135d0061a1f0bmat.def comment ""
position 0 3.75
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236190
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba4063da135d0f7597b92mat.parm {
version 0.8
}
HouNC1033600ba0063da135d0d43f5e73mat.userdata     ___Version___    19.5.493HouNC1033600ba5063da135d03897b9faobj.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display on render on highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236193
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba4063da135d029ff291eobj.parm {
version 0.8
}
HouNC1033600ba0063da135d01274efaaobj.userdata     ___Version___    19.5.493HouNC1033600ba5063da135d0048e5fbeobj.net 1
HouNC1033600ba5063da135d09156a47cout.def comment ""
position 0 1.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236190
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba4063da135d0d5970f51out.parm {
version 0.8
}
HouNC1033600ba0063da135d0009b79cfout.userdata     ___Version___    19.5.493HouNC1033600ba5063da135d05f48a655out.net 1
HouNC1033600baa063da135d0563971c9ch.def comment ""
position 0 0.75
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236190
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba5063da135d008c4757bch.parm {
version 0.8
}
HouNC1033600ba1063da135d064685c3cch.userdata     ___Version___    19.5.493HouNC1033600baa063da135d01e49fb68ch.net 1
HouNC1033600ba4063da135d076989a5ashop.def comment ""
position 0 2.25
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236190
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba7063da135d02c7d5db5shop.parm {
version 0.8
}
HouNC1033600ba3063da135d0240584c2shop.userdata     ___Version___    19.5.493HouNC1033600ba4063da135d0ca38512fshop.net 1
HouNC1033600ba5063da135d0c132d202img.def comment ""
position 0 3
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236191
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba4063da135d00c04e9b6img.parm {
version 0.8
}
HouNC1033600ba0063da135d0c0f67cc3img.userdata     ___Version___    19.5.493HouNC1033600ba2063da135d04ae9db06img/comp1.init type = img
matchesdef = 0
HouNC1033600ba3063da135d0e2aa0b26img/comp1.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236189
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba2063da135d027482685img/comp1.parm {
version 0.8
}
HouNC1033600bbe063da135d03d76e141img/comp1.userdata     ___Version___    19.5.493HouNC1033600ba3063da135d04fbca55fimg/comp1.net 1
HouNC1033600ba5063da135d0e8f4ceb3img.net 1
HouNC1033600ba5063da135d03d423678vex.net 1
HouNC1033600ba5063da135d04f7fd12dmat.net 1
HouNC1033600ba7063da135d0134c5951stage.def comment ""
position 0 4.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on debug off
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236190
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba6063da135d089b12200stage.parm {
version 0.8
pinnedprims	[ 0	locks=0 ]	(	""	)
resolvercontextassetpath	[ 0	locks=0 ]	(	""	)
insertionpointdescriptor	[ 0	locks=0 ]	(	""	)
rendergallerysource	[ 0	locks=0 ]	(	$HIP/galleries/$HIPNAME.$OS/rendergallery.db	)
}
HouNC1033600ba2063da135d0c521ad85stage.userdata     ___Version___    19.5.493HouNC1033600bbc063da135d06bf67a33stage.datablocks         __onload__.expansion 	expansion       {
	"expanded":true
}
 __onload__.loadmasks 	loadmasks       g{
	"populateall":true,
	"populatepaths":[
	],
	"mutelayers":[
	],
	"loadall":true,
	"loadpaths":[
	]
}
HouNC1033600ba7063da135d085fbb0d4stage.net 1
HouNC1033600ba7063da135d03a684e04tasks.def comment ""
position 0 5.25
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236191
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600ba6063da135d07ddb51d6tasks.parm {
version 0.8
}
HouNC1033600ba2063da135d0967a83e6tasks.userdata     ___Version___    19.5.493HouNC1033600bbe063da135d01ea51163tasks/topnet1.init type = topnet
matchesdef = 0
HouNC1033600bbf063da135d000d0965atasks/topnet1.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress off colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236192
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
HouNC1033600bbe063da135d0744b454atasks/topnet1.parm {
version 0.8
cookcontrolssection	[ 0	locks=0 ]	(	0	)
generatestatic	[ 0	locks=0 ]	(	0	)
cookbutton	[ 0	locks=0 ]	(	0	)
dirtybutton	[ 0	locks=0 ]	(	0	)
cancelbutton	[ 0	locks=0 ]	(	0	)
taskgraphsection	[ 0	locks=0 ]	(	0	)
savetaskgraph	[ 0	locks=0 ]	(	0	)
loadtaskgraph	[ 0	locks=0 ]	(	0	)
taskgraphfile	[ 0	locks=0 ]	(	$HIP/$HIPNAME.taskgraph.$F.py	)
taskgraphautosave	[ 0	locks=0 ]	(	"off"	)
taskgraphsaverate	[ 0	locks=0 ]	(	10	)
savegraphattribs	[ 0	locks=0 ]	(	"on"	)
schedulersection	[ 0	locks=0 ]	(	0	)
topscheduler	[ 0	locks=0 ]	(	localscheduler	)
usedefaultlabel	[ 0	locks=0 ]	(	"off"	)
defaultlabel	[ 0	locks=0 ]	(	$OS.`@pdg_index`	)
sep1	[ 0	locks=0 ]	(	)
regenerationtype	[ 0	locks=0 ]	(	"0"	)
evaluationtime	[ 0	locks=0 ]	(	"0"	)
customtime	[ 0	locks=0 ]	(	0	)
savescenefile	[ 0	locks=0 ]	(	"on"	)
}
HouNC1033600bba063da135d07f8642fatasks/topnet1.userdata     ___Version___    19.5.493HouNC1033600b8f063da135d025393678tasks/topnet1/localscheduler.init type = localscheduler
matchesdef = 0
HouNC1033600b8c063da135d0a7224445tasks/topnet1/localscheduler.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display on render on highlight off unload off savedata off compress off colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1675236189
  modify 1675236194
  author rapa@rapalab03
  access 0777
}
color UT_Color RGB 0.478 0.478 0.478 
delscript ""
exprlanguage hscript
end
HouNC1033600b8f063da135d0b3159809tasks/topnet1/localscheduler.parm {
version 0.8
folder0	[ 0	locks=0 ]	(	0	0	0	)
folder5	[ 0	locks=0 ]	(	0	)
maxprocsmenu	[ 0	locks=0 ]	(	"0"	)
maxprocs	[ 0	locks=0 ]	(	1	)
verbose	[ 0	locks=0 ]	(	"off"	)
pdg_waitforfailures	[ 0	locks=0 ]	(	"off"	)
folder4	[ 0	locks=0 ]	(	0	)
pdg_workingdir	[ 0	locks=0 ]	(	$HIP	)
pdg_workitemdatasource	[ 0	locks=0 ]	(	"0"	)
pdg_compressworkitemdata	[ 0	locks=0 ]	(	"on"	)
pdg_validateoutputs	[ 0	locks=0 ]	(	"on"	)
pdg_checkexpectedoutputs	[ 0	locks=0 ]	(	"on"	)
sepparm2	[ 0	locks=0 ]	(	)
pdg_mapmode	[ 0	locks=0 ]	(	"0"	)
pdg_usemapzone	[ 0	locks=0 ]	(	"off"	)
pdg_mapzone	[ 0	locks=0 ]	(	$PDG_PATHMAP_ZONE	)
sepparm3	[ 0	locks=0 ]	(	)
folder1	[ 0	locks=0 ]	(	0	)
tempdirmenu	[ 0	locks=0 ]	(	"1"	)
tempdirappendpid	[ 0	locks=0 ]	(	"on"	)
tempdircustom	[ 0	locks=0 ]	(	$HOUDINI_TEMP_DIR/$HIPNAME/pdgtemp	)
socketcallbacks	[ 0	locks=0 ]	(	1	)
pdg_rpcignoreerrors	[ 0	locks=0 ]	(	"0"	)
pdg_rpctimeout	[ 0	locks=0 ]	(	4	)
pdg_rpcretries	[ 0	locks=0 ]	(	2	)
pdg_rpcbackoff	[ 0	locks=0 ]	(	2	)
pdg_rpcbatch	[ 0	locks=0 ]	(	1	)
pdg_rpcrelease	[ 0	locks=0 ]	(	"on"	)
folder0_2	[ 0	locks=0 ]	(	0	)
local_single	[ 0	locks=0 ]	(	"off"	)
local_is_CPU_number_set	[ 0	locks=0 ]	(	"off"	)
local_CPUs_to_use	[ 0	locks=0 ]	(	1	)
folder6	[ 0	locks=0 ]	(	0	)
local_useminfreemem	[ 0	locks=0 ]	(	"0"	)
local_minfreemem	[ 0	locks=0 ]	(	0	)
local_minfreemempct	[ 0	locks=0 ]	(	0	)
folder2	[ 0	locks=0 ]	(	0	)
local_enabletimeout	[ 0	locks=0 ]	(	"off"	)
local_maxtime	[ 0	locks=0 ]	(	0	)
local_handletimeout	[ 0	locks=0 ]	(	"0"	)
sepparm4	[ 0	locks=0 ]	(	)
local_echandleby	[ 0	locks=0 ]	(	"0"	)
local_echandleall	[ 0	locks=0 ]	(	"on"	)
local_eccustomcode	[ 0	locks=0 ]	(	1	)
sepparm	[ 0	locks=0 ]	(	)
local_maximumretries	[ 0	locks=0 ]	(	3	)
local_addfailcountattr	[ 0	locks=0 ]	(	"off"	)
local_failcountattr	[ 0	locks=0 ]	(	failurecount	)
folder3	[ 0	locks=0 ]	(	0	)
local_usehoudinimaxthreads	[ 0	locks=0 ]	(	"off"	)
local_houdinimaxthreads	[ 0	locks=0 ]	(	0	)
local_requireswindow	[ 0	locks=0 ]	(	"off"	)
local_skippackages	[ 0	locks=0 ]	(	"on"	)
local_envunset	[ 0	locks=0 ]	(	""	)
local_envmulti	[ 0	locks=0 ]	(	0	)
}
HouNC1033600b8b063da135d0270f4441tasks/topnet1/localscheduler.userdata     ___Version___    1HouNC1033600bbf063da135d037bae678tasks/topnet1.net 1
HouNC1033600ba7063da135d0cc34da38tasks.net 1
HouNC1033600ba0063da135d0babaa244.application compproject -r 1920 1080 -a 1 -d fp16 -p 0 1 -P full -f 0 -F 0 -l on
texcache  -a off -r 2147483647 2147483647 -m 10000 -M 15987
shopvisible +I3D +VMantra +RIB
HouNC1033600baa063da135d0bf442759.takes HoudiniTakeFile 1.0
take name Main kids 0
   e
HouNC1033600ba5063da135d06cd4f6d0.styles NSJb{}HouNC1033600bbd063da135d03504820d.contextoptions [
]
HouNC1033600ba8063da135d024f702c4.cwd opcf /
takeset Main
HouNC1033600bba063da135d08919230fNON_COMMERCIAL_FILE!!! 