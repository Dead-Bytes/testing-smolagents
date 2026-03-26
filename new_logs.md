1774523845361 [app/src/shared/memory/MemoryOptimizer.ts:202] DEBUG: 	📊 Memory: RSS 322MB (+50MB), Heap 129MB (+6MB)
1774523875320 [app/src/shared/memory/MemoryOptimizer.ts:202] DEBUG: 	📊 Memory: RSS 322MB (+50MB), Heap 129MB (+6MB)
1774523875366 [app/src/shared/memory/MemoryOptimizer.ts:202] DEBUG: 	📊 Memory: RSS 322MB (+50MB), Heap 129MB (+6MB)
2026-03-26T11:18:00.800Z [app/src/queue-v2/services/RecoveryManager.ts:78] INFO: 	Starting recovery process...
2026-03-26T11:18:00.801Z [app/src/queue-v2/services/RecoveryManager.ts:79] INFO: 	[RecoveryManager] ℹ️  Scope: knowledge pipeline jobs only (GITHUB_V2, PDF_V2, WEBSITE_V2, CUSTOM, etc.)
2026-03-26T11:18:01.152Z [app/src/queue-v2/services/RecoveryManager.ts:746] INFO: 	🔍 Searching for incomplete GitHub V2 knowledge (now: 2026-03-26T11:18:01.151Z, timeout: 300000ms)
2026-03-26T11:18:01.493Z [app/src/queue-v2/services/RecoveryManager.ts:780] INFO: 	🔍 Found 0 incomplete GitHub V2 knowledge bases
2026-03-26T11:18:01.494Z [app/src/queue-v2/services/RecoveryManager.ts:153] INFO: 	Recovery completed in 694ms: {"knowledgeChecked":0,"nodesRecovered":0,"jobsCreated":{"raw":0,"chunking":0,"indexing":0},"errors":0}
2026-03-26T11:18:20.835Z [app/src/utils/authUtils.ts:47] INFO: 	Decoded token: {"org":null,"user":"778292c5-ff68-4fd0-b0a4-b06748e186b5","iat":1774522069}
2026-03-26T11:18:21.176Z [app/src/server/routes/knowledge/customContextRoutes.ts:35] INFO: 	[API] addCustomContext: org=sei repo=https://bytebell-admin@bitbucket.org/bytebell/test1 branch=main
1774523901516 [app/src/core/services/KnowledgeService.ts:173] DEBUG: 	📖 Knowledge retrieved by repoUrl: https://bytebell-admin@bitbucket.org/bytebell/test1
2026-03-26T11:18:21.519Z [app/src/queue-v2/services/CustomContextJobService.ts:20] INFO: 	🔧 Enqueuing CustomContext processing job for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523901861 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:21.870Z [app/src/queue-v2/infrastructure/BullMQManager.ts:129] INFO: 	Job published to BullMQ: eeeaec4d-bb94-4c96-9751-f28fc6888bbc (CUSTOM_CONTEXT_PROCESSING) with jobId: CUSTOM_CONTEXT_PROCESSING-1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:21.871Z [app/src/queue-v2/services/CustomContextJobService.ts:37] INFO: 	✅ CustomContext job enqueued: eeeaec4d-bb94-4c96-9751-f28fc6888bbc for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:21.876Z [app/src/queue-v2/services/core/JobProcessorManager.ts:926] INFO: 	📝 Processing CustomContext job: eeeaec4d-bb94-4c96-9751-f28fc6888bbc for knowledge 1332f096-cebb-4c92-8d64-767148e5abe5
1774523902211 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:22.214Z [app/src/server/routes/knowledge/customContextRoutes.ts:92] INFO: 	[API] addCustomContext enqueued: jobId=eeeaec4d-bb94-4c96-9751-f28fc6888bbc knowledge=1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:22.548Z [app/src/packages/business-context/businessContextStrategy.ts:296] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
2026-03-26T11:18:22.549Z [app/src/packages/business-context/businessContextStrategy.ts:297] INFO: 	[BusinessContext] EXECUTING BUSINESS CONTEXT STRATEGY
2026-03-26T11:18:22.549Z [app/src/packages/business-context/businessContextStrategy.ts:298] INFO: 	[BusinessContext]   Knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:22.551Z [app/src/packages/business-context/businessContextStrategy.ts:299] INFO: 	[BusinessContext]   Repo:      bytebell/test1
2026-03-26T11:18:22.551Z [app/src/packages/business-context/businessContextStrategy.ts:300] INFO: 	[BusinessContext]   Text:      34 chars
2026-03-26T11:18:22.551Z [app/src/packages/business-context/businessContextStrategy.ts:301] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
2026-03-26T11:18:22.551Z [app/src/packages/business-context/businessContextStrategy.ts:304] INFO: 	[BusinessContext] Step 1/6: Resolving commit hash...
1774523902883 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523903217 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:23.217Z [app/src/packages/business-context/businessContextStrategy.ts:108] INFO: 	[BusinessContext] Using provided commitHash: 5e4ea54f94d7
1774523903405 [app/src/knowledge/github/versions/v2/storage/neo4j/Neo4jService.ts:284] DEBUG: 	✅ Neo4j query OK | 185ms | records=1 | params=[knowledgeId, commitHash] | MATCH (fn:FileNode {knowledge_id: $knowledgeId, commit_hash: $commitHash}) RETURN count(fn) AS nodeCount LIMIT 1
2026-03-26T11:18:23.407Z [app/src/packages/business-context/businessContextStrategy.ts:123] INFO: 	[BusinessContext] meta-output missing for commit 5e4ea54f94d7, triggering deep pull
2026-03-26T11:18:23.408Z [app/src/packages/business-context/businessContextStrategy.ts:174] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
2026-03-26T11:18:23.408Z [app/src/packages/business-context/businessContextStrategy.ts:175] INFO: 	[BusinessContext] TRIGGERING DEEP PULL for commit 5e4ea54f94d7
2026-03-26T11:18:23.408Z [app/src/packages/business-context/businessContextStrategy.ts:176] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
1774523903741 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523904080 [app/src/core/services/RawService.ts:317] DEBUG: 	📖 Raw version retrieved: 11f8cfa3-1dd7-4cea-a5c3-50389138be4e
1774523904084 [app/src/core/types/raw-schema-config.ts:78] DEBUG: 	Initialized transient versionProgress field for processing
2026-03-26T11:18:24.087Z [app/src/packages/business-context/businessContextStrategy.ts:278] INFO: 	[BusinessContext] Found previous commit: 7384cce4cce1
2026-03-26T11:18:24.094Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:130] INFO: 	Initializing ENHANCED GitHub V2 Coordinator for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.094Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:131] INFO: 	Repository: https://bitbucket.org/bytebell/test1
2026-03-26T11:18:24.094Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:132] INFO: 	Data path: /app/temp
2026-03-26T11:18:24.094Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:133] INFO: 	Job ID: none
2026-03-26T11:18:24.096Z [app/src/knowledge/github/versions/v2/state/GithubStateHelper.ts:37] INFO: 	🗃️ Initialized GitHub State Helper for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.100Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:119] INFO: 	🔄 GitHub V2 Progress Service initialized for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.101Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:180] INFO: 	Enhanced Git V2 Coordinator initialized for provider: bitbucket
2026-03-26T11:18:24.101Z [app/src/packages/business-context/businessContextStrategy.ts:231] INFO: 	[BusinessContext] Deep pull: 7384cce4 → 5e4ea54f
2026-03-26T11:18:24.102Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:911] INFO: 	Starting ENHANCED GitHub V2 DEEP PULL pipeline for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.104Z [app/src/knowledge/github/versions/v2/progress/ProgressManager.ts:27] INFO: 	📊 ProgressManager initialized with GithubV2ProgressService
2026-03-26T11:18:24.105Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:129] INFO: 	🚀 Starting GitHub V2 processing for: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523904442 [app/src/core/services/KnowledgeService.ts:323] DEBUG: 	✅ Knowledge status updated: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523904446 [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:601] DEBUG: 	📊 Enhanced GitHub V2 status update: PROCESSING 5% - GitHub V2 processing started
1774523904448 [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:764] DEBUG: 	📊 Periodic regression checks started for 1332f096-cebb-4c92-8d64-767148e5abe5 (every 30s - NORMAL frequency)
2026-03-26T11:18:24.448Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:157] INFO: 	✅ GitHub V2 processing status set to PROCESSING with anti-regression monitoring
1774523904450 [app/src/core/utils/schemaValidation.ts:248] DEBUG: 	✅ Knowledge object validation passed for 1332f096-cebb-4c92-8d64-767148e5abe5
1774523904790 [app/src/core/services/KnowledgeService.ts:140] DEBUG: 	✅ Knowledge updated: 1332f096-cebb-4c92-8d64-767148e5abe5 (v5 -> v6)
2026-03-26T11:18:24.791Z [app/src/knowledge/github/update/orchestrators/pipelineRunner.ts:109] INFO: 	Initializing enhanced pipeline components...
2026-03-26T11:18:24.796Z [app/src/knowledge/github/versions/v2/utils/BatchProcessingTracker.ts:303] INFO: 	📂 Loaded existing tracker data with 4 batches
2026-03-26T11:18:24.796Z [app/src/knowledge/github/versions/v2/utils/BatchProcessingTracker.ts:254] INFO: 	📊 BatchProcessingTracker initialized for pipeline: github-v2-1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.797Z [app/src/knowledge/github/update/orchestrators/pipelineRunner.ts:114] INFO: 	Batch Processing Tracker initialized for pipeline: github-v2-1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.798Z [app/src/knowledge/github/update/orchestrators/pipelineRunner.ts:124] INFO: 	Recovery state manager initialized
2026-03-26T11:18:24.800Z [app/src/knowledge/github/versions/v2/memory/AdaptiveMemoryManager.ts:89] INFO: 	🧠 AdaptiveMemoryManager: Starting monitoring
2026-03-26T11:18:24.801Z [app/src/knowledge/github/versions/v2/memory/AdaptiveMemoryManager.ts:90] INFO: 	   Warning: 800MB
2026-03-26T11:18:24.801Z [app/src/knowledge/github/versions/v2/memory/AdaptiveMemoryManager.ts:91] INFO: 	   Critical: 1200MB
2026-03-26T11:18:24.801Z [app/src/knowledge/github/versions/v2/memory/AdaptiveMemoryManager.ts:92] INFO: 	   Absolute: 1400MB
2026-03-26T11:18:24.802Z [app/src/knowledge/github/update/orchestrators/pipelineRunner.ts:139] INFO: 	Adaptive memory manager initialized and monitoring started
2026-03-26T11:18:24.806Z [app/src/knowledge/github/update/orchestrators/pipelineRunner.ts:141] INFO: 	Pipeline state initialized
2026-03-26T11:18:24.807Z [app/src/knowledge/github/versions/v2/executeOrgGithub.ts:952] INFO: 	[DeepPull] Bitbucket fileserver streaming mode — delegating clone to fileserver
2026-03-26T11:18:24.810Z [app/src/knowledge/github/versions/v2/utils/gitUtils.ts:53] INFO: 	🔓 Decrypting Bitbucket token for authentication
1774523904812 [app/src/utils/crypto/simpleCrypto.ts:100] DEBUG: 	🔓 Decrypting GitHub token for knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523904815 [app/src/utils/crypto/simpleCrypto.ts:134] DEBUG: 	✅ GitHub token decrypted successfully
2026-03-26T11:18:24.816Z [app/src/knowledge/github/versions/v2/utils/gitUtils.ts:87] INFO: 	🔑 Using Bitbucket API token (x-bitbucket-api-token-auth)
2026-03-26T11:18:24.816Z [app/src/knowledge/github/versions/v2/utils/gitUtils.ts:79] INFO: 	🔗 Authenticated URL: https://x-bitbucket-api-token-auth:ATATT3xFfGF0vNHPc6IefabjSmY2wLZEKllYT6-vEGJ7qhibyE-8iR4TeClZGjB4UjDjdKGOkEkrxkDxR2K2XC_ucd24GQ1QL4tKOLxNkBAKamIGR47kHJaD9j8QFC8iUz9MigN_GqUwKjJF_fne4akWy6z2BWkZt73zNMF_Ig_ZS6fRsmcN694%3D021D9837@bitbucket.org/bytebell/test1
2026-03-26T11:18:24.817Z [app/src/knowledge/github/versions/v2/storage/FileServerCloneClient.ts:54] INFO: 	FileServerCloneClient: enabled — endpoint http://host.docker.internal:9000
2026-03-26T11:18:24.818Z [app/src/knowledge/github/versions/v2/storage/FileServerCloneClient.ts:93] INFO: 	[FileServerCloneClient] Requesting clone for knowledgeId=1332f096-cebb-4c92-8d64-767148e5abe5 branch=main at commit 5e4ea54f
2026-03-26T11:18:24.826Z [app/src/knowledge/github/versions/v2/storage/FileServerCloneClient.ts:125] ERROR: 	[FileServerCloneClient] clone error: fetch failed
2026-03-26T11:18:24.828Z [app/src/knowledge/github/versions/v2/ExecuteOrgGithub/pipelineFinalization.ts:302] ERROR: 	GitHub V2 pipeline failed [DeepPull] Fileserver clone at 5e4ea54f failed
2026-03-26T11:18:24.829Z [app/src/knowledge/github/versions/v2/utils/HeartbeatLogger.ts:263] INFO: 	💓 [HEARTBEAT] Stopped all operations
2026-03-26T11:18:24.829Z [app/src/knowledge/github/versions/v2/memory/AdaptiveMemoryManager.ts:111] INFO: 	🧠 AdaptiveMemoryManager: Stopped monitoring
1774523904829 [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:776] DEBUG: 	📊 Periodic regression checks stopped for 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:24.830Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:410] ERROR: 	❌ GitHub V2 processing failed: [DeepPull] Fileserver clone at 5e4ea54f failed
1774523905167 [app/src/core/services/KnowledgeService.ts:323] DEBUG: 	✅ Knowledge status updated: 1332f096-cebb-4c92-8d64-767148e5abe5
1774523905168 [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:601] DEBUG: 	📊 Enhanced GitHub V2 status update: FAILED 5% - GitHub V2 processing failed: [DeepPull] Fileserver clone at 5e4ea54f failed
1774523905322 [app/src/shared/memory/MemoryOptimizer.ts:202] DEBUG: 	📊 Memory: RSS 322MB (+50MB), Heap 133MB (+10MB)
1774523905365 [app/src/shared/memory/MemoryOptimizer.ts:202] DEBUG: 	📊 Memory: RSS 322MB (+50MB), Heap 133MB (+10MB)
1774523905505 [app/src/core/services/KnowledgeService.ts:350] DEBUG: 	✅ Knowledge available status updated: 1332f096-cebb-4c92-8d64-767148e5abe5 = false
2026-03-26T11:18:25.506Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:426] INFO: 	❌ Knowledge marked as unavailable due to failure: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:25.507Z [app/src/knowledge/github/versions/v2/progress/GithubV2ProgressService.ts:431] ERROR: 	❌ Processing failed: 1332f096-cebb-4c92-8d64-767148e5abe5 - GitHub V2 processing failed: [DeepPull] Fileserver clone at 5e4ea54f failed
2026-03-26T11:18:25.512Z [app/src/knowledge/github/versions/v2/ExecuteOrgGithub/helperMethods.ts:294] INFO: 	Step manifest written: /app/logs/orgs/sei/bitbucket/v2/1332f096-cebb-4c92-8d64-767148e5abe5/bytebell/test1/pipeline.manifest.json
2026-03-26T11:18:25.512Z [app/src/queue-v2/services/core/JobProcessorManager.ts:979] ERROR: 	❌ CustomContext job eeeaec4d-bb94-4c96-9751-f28fc6888bbc failed: [BusinessContext] Deep pull failed: [DeepPull] Fileserver clone at 5e4ea54f failed
2026-03-26T11:18:25.849Z [app/src/queue-v2/infrastructure/BullMQManager.ts:152] ERROR: 	Job processing failed in BullMQ: eeeaec4d-bb94-4c96-9751-f28fc6888bbc [BusinessContext] Deep pull failed: [DeepPull] Fileserver clone at 5e4ea54f failed
2026-03-26T11:18:25.872Z [app/src/queue-v2/infrastructure/BullMQManager.ts:175] ERROR: 	BullMQ job CUSTOM_CONTEXT_PROCESSING-1332f096-cebb-4c92-8d64-767148e5abe5 failed: [BusinessContext] Deep pull failed: [DeepPull] Fileserver clone at 5e4ea54f failed
2026-03-26T11:18:30.885Z [app/src/queue-v2/services/core/JobProcessorManager.ts:926] INFO: 	📝 Processing CustomContext job: eeeaec4d-bb94-4c96-9751-f28fc6888bbc for knowledge 1332f096-cebb-4c92-8d64-767148e5abe5
1774523911219 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:31.557Z [app/src/packages/business-context/businessContextStrategy.ts:296] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
2026-03-26T11:18:31.559Z [app/src/packages/business-context/businessContextStrategy.ts:297] INFO: 	[BusinessContext] EXECUTING BUSINESS CONTEXT STRATEGY
2026-03-26T11:18:31.559Z [app/src/packages/business-context/businessContextStrategy.ts:298] INFO: 	[BusinessContext]   Knowledge: 1332f096-cebb-4c92-8d64-767148e5abe5
2026-03-26T11:18:31.559Z [app/src/packages/business-context/businessContextStrategy.ts:299] INFO: 	[BusinessContext]   Repo:      bytebell/test1
2026-03-26T11:18:31.560Z [app/src/packages/business-context/businessContextStrategy.ts:300] INFO: 	[BusinessContext]   Text:      34 chars
2026-03-26T11:18:31.560Z [app/src/packages/business-context/businessContextStrategy.ts:301] INFO: 	[BusinessContext] ═══════════════════════════════════════════════
2026-03-26T11:18:31.560Z [app/src/packages/business-context/businessContextStrategy.ts:304] INFO: 	[BusinessContext] Step 1/6: Resolving commit hash...
1774523911893 [app/src/core/services/KnowledgeService.ts:198] DEBUG: 	📖 Knowledge retrieved: 1332f096-cebb-4c92-8d64-767148e5abe5
