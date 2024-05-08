# Copyright (c) 2024, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

header = """/*
 * Copyright (c) 2024, NVIDIA CORPORATION.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/*
 * NOTE: this file is generated by generate_ivf_flat.py
 *
 * Make changes there and run in this directory:
 *
 * > python generate_ivf_flat.py
 *
 */

#include <cuvs/neighbors/ivf_flat.hpp>
"""

build_include_macro = """
#include "ivf_flat_build.cuh"
"""
search_include_macro = """
#include "ivf_flat_search.cuh"
"""

serialize_include_macro = """
#include "ivf_flat_serialize.cuh"
"""

namespace_macro = """
namespace cuvs::neighbors::ivf_flat {
"""

footer = """
}  // namespace cuvs::neighbors::ivf_flat
"""

types = dict(
    float_int64_t=("float", "int64_t"),
    int8_t_int64_t=("int8_t", "int64_t"),
    uint8_t_int64_t=("uint8_t", "int64_t"),
)

build_macro = """
#define CUVS_INST_IVF_FLAT_BUILD(T, IdxT)                                                      \\
  auto build(raft::resources const& handle,                                                    \\
             const cuvs::neighbors::ivf_flat::index_params& params,                            \\
             raft::device_matrix_view<const T, IdxT, raft::row_major> dataset)                 \\
    ->cuvs::neighbors::ivf_flat::index<T, IdxT>                                                \\
  {                                                                                            \\
    return cuvs::neighbors::ivf_flat::index<T, IdxT>(                                          \\
      std::move(cuvs::neighbors::ivf_flat::detail::build(handle, params, dataset)));          \\
  }                                                                                            \\
                                                                                               \\
  void build(raft::resources const& handle,                                                    \\
             const cuvs::neighbors::ivf_flat::index_params& params,                            \\
             raft::device_matrix_view<const T, IdxT, raft::row_major> dataset,                 \\
             cuvs::neighbors::ivf_flat::index<T, IdxT>& idx)                                   \\
  {                                                                                            \\
    cuvs::neighbors::ivf_flat::detail::build(handle, params, dataset, idx); \\
  } \\
  auto build(raft::resources const& handle,                                                    \\
             const cuvs::neighbors::ivf_flat::index_params& params,                            \\
             raft::host_matrix_view<const T, IdxT, raft::row_major> dataset)                 \\
    ->cuvs::neighbors::ivf_flat::index<T, IdxT>                                                \\
  {                                                                                            \\
    return cuvs::neighbors::ivf_flat::index<T, IdxT>(                                          \\
      std::move(cuvs::neighbors::ivf_flat::detail::build(handle, params, dataset)));          \\
  }                                                                                            \\
                                                                                               \\
  void build(raft::resources const& handle,                                                    \\
             const cuvs::neighbors::ivf_flat::index_params& params,                            \\
             raft::host_matrix_view<const T, IdxT, raft::row_major> dataset,                 \\
             cuvs::neighbors::ivf_flat::index<T, IdxT>& idx)                                   \\
  {                                                                                            \\
    cuvs::neighbors::ivf_flat::detail::build(handle, params, dataset, idx); \\
  }
"""

extend_macro = """
#define CUVS_INST_IVF_FLAT_EXTEND(T, IdxT)                                           \\
  auto extend(raft::resources const& handle,                                         \\
              raft::device_matrix_view<const T, IdxT, raft::row_major> new_vectors,  \\
              std::optional<raft::device_vector_view<const IdxT, IdxT>> new_indices, \\
              const cuvs::neighbors::ivf_flat::index<T, IdxT>& orig_index)           \\
    ->cuvs::neighbors::ivf_flat::index<T, IdxT>                                      \\
  {                                                                                  \\
    return cuvs::neighbors::ivf_flat::index<T, IdxT>(                                \\
      std::move(cuvs::neighbors::ivf_flat::detail::extend(                          \\
        handle, new_vectors, new_indices, orig_index)));           \\
  }                                                                                  \\
                                                                                     \\
  void extend(raft::resources const& handle,                                         \\
              raft::device_matrix_view<const T, IdxT, raft::row_major> new_vectors,  \\
              std::optional<raft::device_vector_view<const IdxT, IdxT>> new_indices, \\
              cuvs::neighbors::ivf_flat::index<T, IdxT>* idx)                        \\
  {                                                                                  \\
    cuvs::neighbors::ivf_flat::detail::extend(                                      \\
      handle, new_vectors, new_indices, idx);                      \\
  }    \\
  auto extend(raft::resources const& handle,                                         \\
              raft::host_matrix_view<const T, IdxT, raft::row_major> new_vectors,  \\
              std::optional<raft::host_vector_view<const IdxT, IdxT>> new_indices, \\
              const cuvs::neighbors::ivf_flat::index<T, IdxT>& orig_index)           \\
    ->cuvs::neighbors::ivf_flat::index<T, IdxT>                                      \\
  {                                                                                  \\
    return cuvs::neighbors::ivf_flat::index<T, IdxT>(                                \\
      std::move(cuvs::neighbors::ivf_flat::detail::extend(                          \\
        handle, new_vectors, new_indices, orig_index)));           \\
  }                                                                                  \\
                                                                                     \\
  void extend(raft::resources const& handle,                                         \\
              raft::host_matrix_view<const T, IdxT, raft::row_major> new_vectors,  \\
              std::optional<raft::host_vector_view<const IdxT, IdxT>> new_indices, \\
              cuvs::neighbors::ivf_flat::index<T, IdxT>* idx)                        \\
  {                                                                                  \\
    cuvs::neighbors::ivf_flat::detail::extend(                                      \\
      handle, new_vectors, new_indices, idx);                      \\
  }                    
"""

search_macro = """
#define CUVS_INST_IVF_FLAT_SEARCH(T, IdxT)                                      \\
  void search(raft::resources const& handle,                                    \\
              const cuvs::neighbors::ivf_flat::search_params& params,           \\
              cuvs::neighbors::ivf_flat::index<T, IdxT>& index,                 \\
              raft::device_matrix_view<const T, IdxT, raft::row_major> queries, \\
              raft::device_matrix_view<IdxT, IdxT, raft::row_major> neighbors,  \\
              raft::device_matrix_view<float, IdxT, raft::row_major> distances) \\
  {                                                                             \\
    cuvs::neighbors::ivf_flat::detail::search(                                 \\
      handle, params, index, queries, neighbors, distances);  \\
  }
"""

serialize_macro = """
#define CUVS_INST_IVF_FLAT_SERIALIZE(T, IdxT)                                                      \\
  void serialize_file(raft::resources const& handle,                                               \\
                      const std::string& filename,                                                 \\
                      const cuvs::neighbors::ivf_flat::index<T, IdxT>& index)                      \\
  {                                                                                                \\
    cuvs::neighbors::ivf_flat::detail::serialize(handle, filename, index); \\
  }                                                                                                \\
                                                                                                   \\
  void deserialize_file(raft::resources const& handle,                                             \\
                        const std::string& filename,                                               \\
                        cuvs::neighbors::ivf_flat::index<T, IdxT>* index)                          \\
  {                                                                                                \\
    * index = cuvs::neighbors::ivf_flat::detail::deserialize<T, IdxT>(                                          \\
      handle, filename);                                                  \\
  }                                                                                                
"""

macros = dict(
    build=dict(
        include=build_include_macro,
        definition=build_macro,
        name="CUVS_INST_IVF_FLAT_BUILD",
    ),
    extend=dict(
        include=build_include_macro,
        definition=extend_macro,
        name="CUVS_INST_IVF_FLAT_EXTEND",
    ),
    search=dict(
        include=search_include_macro,
        definition=search_macro,
        name="CUVS_INST_IVF_FLAT_SEARCH",
    ),
    serialize=dict(
        include=serialize_include_macro,
        definition=serialize_macro,
        name="CUVS_INST_IVF_FLAT_SERIALIZE",
    ),
)

for type_path, (T, IdxT) in types.items():
    for macro_path, macro in macros.items():
        path = f"ivf_flat_{macro_path}_{type_path}.cu"
        with open(path, "w") as f:
            f.write(header)
            f.write(macro['include'])
            f.write(namespace_macro)
            f.write(macro["definition"])
            f.write(f"{macro['name']}({T}, {IdxT});\n\n")
            f.write(f"#undef {macro['name']}\n")
            f.write(footer)

        print(f"src/neighbors/ivf_flat/{path}")
